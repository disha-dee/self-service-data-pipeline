import pandas as pd
import json
from pathlib import Path
from datetime import datetime


# -----------------------------
# Apply schema mapping
# -----------------------------
def apply_mapping(df):

    config_path = Path("configs/mapping.json")

    with open(config_path) as f:
        mapping = json.load(f)

    df_transformed = df.rename(columns=mapping)

    return df_transformed


# -----------------------------
# Save data to Data Lake
# -----------------------------
def save_to_datalake(df_raw, df_clean):

    bronze_path = Path("data_lake/bronze/raw_data.csv")
    silver_path = Path("data_lake/silver/clean_data.csv")

    bronze_path.parent.mkdir(parents=True, exist_ok=True)
    silver_path.parent.mkdir(parents=True, exist_ok=True)

    df_raw.to_csv(bronze_path, index=False)
    df_clean.to_csv(silver_path, index=False)


# -----------------------------
# Log pipeline run metadata
# -----------------------------
def log_pipeline_run(rows_processed, status):

    metadata_path = Path("metadata/pipeline_runs.csv")

    metadata_path.parent.mkdir(exist_ok=True)

    run_data = pd.DataFrame([{
        "timestamp": datetime.now(),
        "rows_processed": rows_processed,
        "status": status
    }])

    if metadata_path.exists():
        existing = pd.read_csv(metadata_path)
        df = pd.concat([existing, run_data], ignore_index=True)
    else:
        df = run_data

    df.to_csv(metadata_path, index=False)


# -----------------------------
# Create Gold Layer
# -----------------------------
def create_gold_layer(df_clean):

    gold_path = Path("data_lake/gold/department_salary_summary.csv")

    gold_path.parent.mkdir(parents=True, exist_ok=True)

    gold_df = df_clean.groupby("department").agg(
        total_salary=("salary", "sum"),
        employee_count=("employee_id", "count")
    ).reset_index()

    gold_df.to_csv(gold_path, index=False)

    return gold_df