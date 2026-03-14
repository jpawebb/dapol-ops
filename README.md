# DapolOps: Production Data Platform for Model Train Inventory Management
![dbt CI](https://github.com/jpawebb/dapol-ops/actions/workflows/dbt_ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![dbt Version](https://img.shields.io/badge/dbt-1.11.x-orange)
![Database](https://img.shields.io/badge/Database-PostgreSQL%20(Neon)-00A3FF)
![Registry Count](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/jpawebb/52696f4cc2409a384edce3e16955c875/raw/dapol_stats.json)


![dapol-logo](images/dapol-logo.avif)


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


## Resources:
1. [Hampshire Models](https://www.hampshiremodels.co.uk/collections/dapol/oo?page=4)
2. [New Modellsshop](https://www.newmodellersshop.co.uk/dapol-wagons.htm)
3. [Rails of Sheffield](https://railsofsheffield.com/search?q=Dapol+OO+Somerset&options%5Bprefix%5D=last)
4. [Model Railway Emporium](https://modelrailwayemporium.com/collections/dapol-00-gauge-wagons-1?page=13)
5. [PicClick](https://picclick.co.uk/New-Dapol-Limited-Edition-Wagon-Somerset-Trading-Co-254110704972.html)

## TODO:
- Add charity for profit
    1. Add dim_/ stg_charities models and join to marts on models.id
    2. Evolve the models schema to add charity_beneficiary
    3. Other

| neondb_id | charity |
|--------|--------|
| 19 | St. Margrets Hospice Care |

