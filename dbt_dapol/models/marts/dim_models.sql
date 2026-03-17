{{ 
    config(materialized='table')
 }}

with models as (
    select * from {{ ref('stg_models') }}
),

charities as (
    select * from {{ ref('stg_charities') }}
)

select
    id as model_id,
    full_title,
    dapol_product_code,
    model_type,
    model_subtype,

    case
        when model_type = 'Wagon' then 'Rolling Stock'
        when model_type in ('Steam', 'Diesel') then 'Locomotive'
        else 'Accessories'
    end as category_group,

    description,
    first_extracted_url as extracted_url,
    livery_company,
    running_number,
    edition_no,
    total_edition_limit,

    -- Charity info
    c.charity_name,

    date_catalogued,
    scale,
    coupling_type,
    dcc_status,
    physical_condition,
    box_condition,

    estimated_value,
    min_acceptable_price,

    created_at,
    updated_at

from models m
left join charities c on c.charity_id = m.charity_id