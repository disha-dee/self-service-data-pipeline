# Self-Service Data Pipeline Platform

An end-to-end **Data Engineering project** that allows users to upload datasets, map schemas dynamically, and run automated data pipelines using the **Medallion Architecture (Bronze → Silver → Gold)**.

This project demonstrates how modern data platforms ingest raw data, transform it, generate analytics-ready datasets, and monitor pipeline executions.

---

# Overview

The platform provides a **user-friendly web interface** built with Streamlit where users can:

- Upload datasets
- Map dataset columns to a standardized schema
- Execute data transformation pipelines
- Store data in Bronze, Silver, and Gold layers
- Monitor pipeline execution history

This project mimics how real-world **data lake pipelines** operate in modern data platforms such as **Azure Databricks, Snowflake, and Delta Lake**.

---

# Architecture

The pipeline follows the **Medallion Data Architecture**:

User Upload  
↓  
Schema Mapping  
↓  
Bronze Layer (Raw Data)  
↓  
Silver Layer (Clean Data)  
↓  
Gold Layer (Business Analytics)  
↓  
Pipeline Monitoring Dashboard

### Layer Explanation

**Bronze Layer**

- Stores raw ingested datasets
- Acts as immutable source data

**Silver Layer**

- Cleans and standardizes the dataset
- Applies schema mapping

**Gold Layer**

- Produces aggregated analytics datasets
- Used for dashboards and reporting

---

# Features

- Streamlit-based data ingestion interface
- Dynamic column mapping system
- Medallion architecture implementation
- Bronze, Silver, and Gold data layers
- Modular transformation engine
- Pipeline execution metadata logging
- Pipeline monitoring dashboard
- Error handling and pipeline status tracking

---

# Tech Stack

Python  
Streamlit  
Pandas  
Git

Future cloud integrations:

Azure Data Lake Storage  
Azure Databricks  
Azure Data Factory

---

# Project Structure

self-service-data-platform

website/  
└── app.py (Streamlit ingestion UI)

mapping_engine/  
└── transform.py (data transformation logic)

configs/  
└── mapping.json (schema mapping configuration)

data_lake/  
├── bronze  
├── silver  
└── gold

metadata/  
└── pipeline_runs.csv

data_sample/  
└── employees.csv

pyproject.toml  
uv.lock  
README.md

---

# How the Pipeline Works

### Step 1 – Upload Dataset

The user uploads a CSV dataset through the Streamlit interface.

Example dataset:

empid,dept,salary  
101,IT,60000  
102,HR,50000  
103,Finance,70000

---

### Step 2 – Schema Mapping

Users map their dataset columns to a standardized schema.

Example mapping:

empid → employee_id  
dept → department  
salary → salary

Mapping configuration is stored in:

configs/mapping.json

---

### Step 3 – Data Transformation

The pipeline performs:

1. Schema transformation
2. Raw data ingestion
3. Clean dataset generation
4. Analytics aggregation

---

### Step 4 – Data Storage

The pipeline stores data across three layers.

Bronze Layer

data_lake/bronze/raw_data.csv

Silver Layer

data_lake/silver/clean_data.csv

Gold Layer

data_lake/gold/department_salary_summary.csv

---

### Step 5 – Pipeline Monitoring

Each pipeline run is recorded in:

metadata/pipeline_runs.csv

Example log:

timestamp,rows_processed,status  
2026-03-16 00:10:21,8,SUCCESS

The Streamlit dashboard visualizes:

- Pipeline run history
- Rows processed trend

---

# Running the Project

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/self-service-data-pipeline.git
```

Navigate into the project

```bash
cd self-service-data-platform
```

Activate environment

```bash
source .venv/bin/activate
```

Run the application

```bash
uv run streamlit run website/app.py
```

The application will open in your browser:

http://localhost:8501

---

# Example Gold Layer Output

department,total_salary,employee_count

IT,125000,2  
HR,50000,1  
Finance,70000,1

This dataset is **analytics-ready and suitable for BI dashboards**.

---

# Future Improvements

Planned upgrades for this project:

- Azure Data Lake Storage integration
- Azure Databricks Spark transformations
- Azure Data Factory pipeline orchestration
- Data quality validation layer
- Automated CI/CD deployment
- Data visualization dashboards

---

# Learning Outcomes

This project demonstrates several **core data engineering concepts**:

- Data ingestion pipelines
- Schema mapping and transformation
- Medallion architecture
- Data lake storage layers
- Pipeline observability
- Data pipeline monitoring

---

# Author

Disha Chandra

Data Engineering project demonstrating ingestion, transformation, analytics, and monitoring in a modern data pipeline architecture.
