select
    sale_id,
    model_id,
    sale_date,
    quantity,
    price_per_unit
from {{ source('raw_dapol', 'raw_sales') }}