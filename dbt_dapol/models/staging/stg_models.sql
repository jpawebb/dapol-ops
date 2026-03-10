with source as (
    select * from {{ source('raw_dapol', 'raw_models') }}
)

select
    cast(id as integer) as model_id,
    trim(name) as model_name,
    dapol_product_code,
    trim(type) as model_type,
    trim(description) as description,
    livery_company,
    running_number,
    limited_edition_no,
    cast(date_catalogued as date) as date_catalogued,
    upper(scale) as scale,
    coupling_type,
    dcc_status,
    physical_condition,
    box_condition,
    cast(estimated_value as numeric(10,2)) as estimated_value,
    cast(min_acceptable_price as numeric(10,2)) as min_acceptable_price,
    cast(created_at as timestamp) as created_at,
    cast(updated_at as timestamp) as updated_at
from source