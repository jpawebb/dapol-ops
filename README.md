# DapolOps: Production Data Platform for Model Train Inventory Management

## Overview
DapolOps is a comprehensive data engieering platform designed to manage, analyse, and track Dapol model train inventory. Built with modern data stack principles, it provides full CRUD operations, data quality assurance, and analytics-ready datasets. 

## Architecture
**Medallion Architecture**
```
📊 STREAMLIT UI → 🗄️ POSTGRESQL (Bronze) → 🔄 dbt (Silver/ Gold) → 📈 ANALYTICS
```
- **Bronze:** Raw data ingestion via Streamlit → PostgreSQL (NeonDB)
- **Silver:** Data cleaning, validation, and staging (dbt)
- **Gold:** Analytics-ready start schema with business logic
- **Orchestration:** GitHub Actions for automated testing and deployment

## Tech Stack
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | Streamlit | Data entry and editing interface |
| **Database** | PostgreSQL (NeonDB) | Data storage and processing |
| **Data Modelling** | dbt Core | Transformation and business logic |
| **CI/CD** | GitHub Actions | Automated testing and deployment |
| **Data Quality** | dbt tests | Validation and integrity checks |
| **Documentation** | dbt docs | Data lineage and catalog |


