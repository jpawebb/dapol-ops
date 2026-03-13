# DapolOps: Production Data Platform for Model Train Inventory Management
![dbt CI](https://github.com/jpawebb/dapol-ops/actions/workflows/dbt_ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![dbt Version](https://img.shields.io/badge/dbt-1.11.x-orange)
![Database](https://img.shields.io/badge/Database-PostgreSQL%20(Neon)-00A3FF)
![Registry Count](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/jpawebb/YOUR_GIST_ID_HERE/raw/dapol_stats.json)


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


## TODO:
- [x] Submit button for form
- Add resource links e.g. 
    - Model shops: https://www.hampshiremodels.co.uk/collections/dapol/oo?page=4, https://www.newmodellersshop.co.uk/dapol-wagons.htm, https://railsofsheffield.com/search?q=Dapol+OO+Somerset&options%5Bprefix%5D=last
    - Emporium: https://modelrailwayemporium.com/collections/dapol-00-gauge-wagons-1?page=13
    - Sales Records: https://picclick.co.uk/New-Dapol-Limited-Edition-Wagon-Somerset-Trading-Co-254110704972.html
- Ticket notes/ Standar conventions e.g. 5-plank and Conflat?
- Jpeg/ png compatibility
- Field Desciptions:
    - Running number (This is the small number printed on the wagon body, usually on the lower plank or near the company lettering.)
    - DCC (not normally relevant to wagons)
    - Coupling (tension‑lock couplings in NEM pockets)
    - Model type (Wagon)
        - Must be a multi-select:
            - Open plank wagons (4‑, 5‑, 7‑, 8‑plank)
            - Vans (Enclosed box vans, salt vans, gunpowder vans, cattle vans)
            - Tank wagons (10–20T tankers, 6‑wheel tanks, dairy and oil company liveries)
            - Hopper/ballast wagons (JHA hoppers, Turbot, IOA, MJA ballast box wagons)
        - Clean scheme is:
            - Category: “Open wagon / Van / Tank / Hopper / Bogie ballast / Specialist”.
            - Sub‑type: “4‑plank”, “Salt van”, “20T tank”, “IOA ballast”, “MJA bogie box”, etc.
    - What is the differerce between Livery Number and Edition number? I can see on the certificate this wagon is Limited Edition Number 2 of 112, and printed on the side of the wagon it says: Somerset Trading Co. Ltd Late Brown & Co. Bridgewater Somerset No.12
- Add charity for profits