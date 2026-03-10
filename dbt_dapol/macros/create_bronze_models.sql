{% macro create_bronze_models() %}

CREATE TABLE bronze.raw_models (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    dapol_product_code TEXT NULL,
    type TEXT NULL,
    description TEXT NULL,
    livery_company TEXT NULL,
    running_number TEXT NULL,
    limited_edition_no TEXT NULL,
    date_catalogued DATE NULL,
    scale TEXT NULL,
    coupling_type TEXT NULL,
    dcc_status TEXT NULL,
    physical_condition TEXT NULL,
    box_condition TEXT NULL,
    estimated_value NUMERIC(10,2) NULL,
    min_acceptable_price NUMERIC(10,2) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

{% endmacro %}