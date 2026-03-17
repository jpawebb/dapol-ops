{{ config(materialized='view') }}

with base as (
    select * from {{ source('raw_dapol', 'raw_models') }}
),

model_categories as (
  select
    *,
    split_part(type, ' - ', 2) as raw_model_subtype
  from base
)

select
    id,
    name as full_title,
    dapol_product_code,

    split_part(type, ' - ', 1) as model_type,

    case
        when raw_model_subtype ILIKE '%ventilated van%' then 'Vent Van'
        when raw_model_subtype ILIKE '%tanker%' then 'Tanker'
        when raw_model_subtype ILIKE '%freight%' then 'Freight'
        when raw_model_subtype ILIKE '%conflat%' or raw_model_subtype ILIKE '%-plank%' then 'Conflat'
        else 'Other'
    end as model_subtype,

    description,
    (regexp_match(description, 'https?://[^\s]+'))[1] as first_extracted_url,

    livery_company,
    coalesce(substring(running_number from '\d+'), 'Unknown') as running_number,

    cast(nullif(split_part(limited_edition_no, ' of ', 1), '') as int) as edition_no,
    cast(nullif(split_part(limited_edition_no, ' of ', 2), '') as int) as total_edition_limit,

    date_catalogued,

    case
        when scale = 'OO' then 'OO Gauge'
        when scale = 'N' then 'N Gauge'
        when scale = 'O' then 'O Gauge'
        else 'Unknown'
    end as scale,

    coupling_type,

    case
        when split_part(type, ' - ', 1) = 'Wagon' then 'N/A' else dcc_status
    end as dcc_status,

    physical_condition,
    box_condition,

    cast(estimated_value as decimal(10,2)) as estimated_value,
    cast(min_acceptable_price as decimal(10,2)) as min_acceptable_price,

    created_at,
    updated_at

from model_categories
