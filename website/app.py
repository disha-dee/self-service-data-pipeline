import streamlit as st
import pandas as pd
import json
import sys
from pathlib import Path

# Fix import path so Python can see project folders
sys.path.append(str(Path(__file__).resolve().parent.parent))

from mapping_engine.transform import (
    apply_mapping,
    save_to_datalake,
    log_pipeline_run,
    create_gold_layer
)

st.title("Self Service Data Pipeline Platform")

st.write("Upload a dataset, map columns, and run the data pipeline.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:

    # ----------------------------
    # DATASET PREVIEW
    # ----------------------------

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    columns = df.columns.tolist()

    # ----------------------------
    # COLUMN MAPPING UI
    # ----------------------------

    st.subheader("Map Columns")

    id_column = st.selectbox("Select Employee ID Column", columns)
    dept_column = st.selectbox("Select Department Column", columns)
    salary_column = st.selectbox("Select Salary Column", columns)

    # ----------------------------
    # SAVE MAPPING CONFIG
    # ----------------------------

    if st.button("Save Mapping"):

        mapping = {
            id_column: "employee_id",
            dept_column: "department",
            salary_column: "salary"
        }

        config_dir = Path("configs")
        config_dir.mkdir(exist_ok=True)

        config_file = config_dir / "mapping.json"

        with open(config_file, "w") as f:
            json.dump(mapping, f, indent=4)

        st.success("Mapping saved successfully!")

        st.write("Mapping configuration:")
        st.json(mapping)

    # ----------------------------
    # RUN PIPELINE TRANSFORMATION
    # ----------------------------

    if st.button("Run Transformation"):

        try:

            # Apply schema mapping
            df_transformed = apply_mapping(df)

            # Save bronze & silver
            save_to_datalake(df, df_transformed)

            # Create gold analytics layer
            gold_df = create_gold_layer(df_transformed)

            # Log pipeline metadata
            log_pipeline_run(len(df_transformed), "SUCCESS")

            st.subheader("Silver Layer (Clean Data)")
            st.dataframe(df_transformed.head())

            st.subheader("Gold Layer Analytics")
            st.dataframe(gold_df)

            st.success("Pipeline completed successfully!")

        except Exception as e:

            log_pipeline_run(0, "FAILED")

            st.error(f"Pipeline failed: {e}")

# ----------------------------
# PIPELINE MONITORING DASHBOARD
# ----------------------------

st.divider()
st.header("Pipeline Run History")

metadata_file = Path("metadata/pipeline_runs.csv")

if metadata_file.exists():

    try:

        runs_df = pd.read_csv(metadata_file)

        if not runs_df.empty:

            st.dataframe(runs_df)

            st.subheader("Rows Processed Trend")

            st.line_chart(runs_df["rows_processed"])

        else:
            st.info("Pipeline log file exists but has no runs yet.")

    except pd.errors.EmptyDataError:
        st.info("Pipeline log file is empty.")

else:

    st.info("No pipeline runs recorded yet.")