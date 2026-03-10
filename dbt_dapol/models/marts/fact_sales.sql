{{
    config(
        materialized='table'
    )
}}

with sales as (
    select * from {{ ref('stg_sales') }}
),

models as (
    select * from {{ ref('dim_models') }}
)

select
    md5(cast(sales.sale_id as text)) as sales_key,
    sales.sale_id,
    sales.model_id,
    sales.sale_date,
    sales.quantity,
    sales.price_per_unit,
    (sales.quantity * sales.price_per_unit) as total_revenue
from sales
inner join models on cast(sales.model_id as integer) = models.model_id