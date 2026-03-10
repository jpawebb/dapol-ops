{{ 
    config(
        materialized='table'
    )
}}

with stg_models as (
    select * from {{ ref('stg_models') }}
)

select
    model_id,
    model_name,
    model_type,
    scale,
    created_at,
    case
        when model_type = 'Steam' then 'Classic'
        else 'Modern'
    end as category_group
from stg_models