# DapolOps: Data Architecture for Rolling Stock Management of Model Trains

## Overview
DapolOps is an automated data engineering platform designed to aggregate, validate, and analyze market trends for Dapol model trains. 

## Architecture
This project utilizes a **Medallion Architecture** to process manual input into actionable insights:

* **Ingestion:** Streamlit UI captures manual inputs and lands raw data in **Google Cloud Storage (Bronze Layer)**.
* **Validation:** Python/Pydantic scripts enforce schema integrity and flag invalid records.
* **Transformation:** **dbt Core** transforms validated data into a **Star Schema** within **Google BigQuery (Silver/Gold Layers)**.
* **Orchestration:** **GitHub Actions** automates the execution of transformation jobs and data quality tests.
* **Reporting:** **Looker Studio** provides real-time trend analysis.

## Tech Stack
* **Languages:** Python (Data Validation, Ingestion)
* **Data Warehouse:** Postgres (Neondb)
* **Data Modeling:** dbt (data build tool)
* **CI/CD:** GitHub Actions

## Key Data Engineering Features
- [ ] **Schema Enforcement:** Prevents dirty data from entering the production warehouse using Pydantic.
- [ ] **Star Schema Design:** Optimized fact and dimension modeling for analytical performance.
- [ ] **Version-Controlled Pipelines:** Entire pipeline logic is managed as code via Git.
- [ ] **Data Lineage:** Clear transformation path from raw ingestion to reporting.

## Data Model (Star Schema)
* **Fact_Sales:** `sale_id`, `date_id`, `model_id`, `sale_price`, `condition_grade`.
* **Dim_Models:** `model_id`, `model_name`, `era`, `livery_type`, `gauge_scale`.
* **Dim_Dates:** `date_id`, `month`, `quarter`, `year`.
