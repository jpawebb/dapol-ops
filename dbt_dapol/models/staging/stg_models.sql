with source as (
    select * from {{ source('raw_dapol', 'raw_models') }}
)

select
    cast(id as integer) as model_id,
    trim(name) as model_name,
    trim(type) as model_type,
    upper(scale) as scale,
    created_at
from source