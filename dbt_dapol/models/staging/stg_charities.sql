{{ config(materialized='view') }}

with source as (
    select * from {{ source('raw_dapol', 'raw_charities') }}
)

select
    id as charity_id,
    trim(charity_name) as charity_name,
    created_at
from source