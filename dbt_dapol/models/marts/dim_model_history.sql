{{ config(materialized='table') }}

with model_changes as (
    select
        id as model_id,
        name as model_name,
        dapol_product_code,
        estimated_value,
        physical_condition,
        box_condition,
        created_at,
        updated_at,
        LAG(estimated_value) OVER (PARTITION BY id ORDER BY updated_at) as previous_value,
        LAG(updated_at) OVER (PARTITION BY id ORDER BY updated_at) as previous_update_date

    from {{ source('raw_dapol', 'raw_models') }}
)

select
    *,
    case
        when previous_value is not null and estimated_value != previous_value
        then (estimated_value - previous_value)
        else null
    end as value_change,

    case
        when previous_update_date is not null
        then extract(days from (updated_at - previous_update_date))
        else null
    end as days_since_update

from model_changes
