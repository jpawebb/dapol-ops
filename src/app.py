from datetime import datetime
import streamlit as st
from sqlalchemy import text
from db_connection import get_engine

# Page setup for a professional look
st.set_page_config(page_title="Dapol Inventory Portal", layout="centered")

st.title("--Dapol Inventory Entry--")
st.markdown("Enter new model details below to ingest data into the **Bronze Layer**.")

# The form container
with st.form("model_entry", clear_on_submit=True):
    # Organising inputs into columns
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Model Name")
        prod_code = st.text_input("Dapol Product Code")
        type_ = st.text_input("Model Type (e.g. Steam, Diesel)")
        livery = st.text_input("Livery Company")
        running = st.text_input("Running Number")

    with col2:
        scale = st.text_input("Scale (e.g. OO, N)")
        coupling = st.text_input("Coupling Type")
        dcc = st.text_input("DCC Status")
        edition = st.text_input("Limited Edition Number")

    description = st.text_area("Description", max_chars=200)

    col3, col4 = st.columns(2)
    with col3:
        physical_condition = st.text_input("Physical Condition")
        price = st.number_input("Estimated Value (£)", min_value=0.0, step=0.01)
    with col4:
        box_condition = st.text_input("Box Condition")
        min_acceptable_price = st.number_input(
            "Min Acceptable Price (£)", min_value=0.0, step=0.01
        )

    # Automatic Timestamp Fields
    date_catalogued = datetime.now().date()
    created_at = datetime.now()
    updated_at = datetime.now()

    submitted = st.form_submit_button("Add to Inventory")

    if submitted:
        try:
            engine = get_engine()

            insert_query = text(
                """
                INSERT INTO bronze.raw_models (
                    name, dapol_product_code, type, description, livery_company, running_number, 
                    limited_edition_no, date_catalogued, scale, coupling_type, dcc_status, 
                    physical_condition, box_condition, estimated_value, min_acceptable_price, 
                    created_at, updated_at
                ) VALUES (
                    :name, :prod_code, :type, :desc, :livery, :running, 
                    :edition, :date_cat, :scale, :coupling, :dcc, 
                    :phys, :box, :est_val, :min_val, 
                    :created, :updated
                )
            """
            )

            params = {
                "name": name,
                "prod_code": prod_code,
                "type": type_,
                "desc": description,
                "livery": livery,
                "running": running,
                "edition": edition,
                "date_cat": date_catalogued,
                "scale": scale,
                "coupling": coupling,
                "dcc": dcc,
                "phys": physical_condition,
                "box": box_condition,
                "est_val": price,
                "min_val": min_acceptable_price,
                "created": created_at,
                "updated": updated_at,
            }

            # 3. Using 'engine.begin()' to auto-commit the transaction
            with engine.begin() as conn:
                conn.execute(insert_query, params)

            st.success(f"Successfully added '{name}' to the database!")
            st.balloons()

        except Exception as e:
            st.error(f"Error ingesting data: {e}")
