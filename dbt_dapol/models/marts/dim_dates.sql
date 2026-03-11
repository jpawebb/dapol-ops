{{ config(materialized='table') }}

with date_spine as (
    {{ dbt_utils.date_spine(
        datepart="day",
        start_date="cast('2025-01-01' as date)",
        end_date="cast('2030-12-31' as date)", 
    )}}
)

select
    date_day as date,
    extract(year from date_day) as year,
    extract(month from date_day) as month,
    extract(quarter from date_day) as quarter,
    extract(dow from date_day) as day_of_week,
    to_char(date_day, 'Month') as month_name,
    to_char(date_day, 'Day') as day_name,

    case 
        when extract(dow from date_day) in (0, 6) then true
        else false
    end as is_weekend
from date_spine