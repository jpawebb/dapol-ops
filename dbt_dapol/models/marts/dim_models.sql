{{ 
    config(materialized='table')
 }}

with base as (
    select * from {{ ref('stg_models') }}
)

select
    *,

    case
        when model_type = 'Steam' then 'Classic'
        else 'Modern'
    end as category_group,
    
    (estimated_value - min_acceptable_price) as potential_profit_margin

from base