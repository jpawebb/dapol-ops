from datetime import datetime
import streamlit as st
from sqlalchemy import text
from db_connection import get_engine

# Page setup for a professional look
st.set_page_config(page_title="Dapol Inventory Portal", layout="wide")

tab1, tab2 = st.tabs(["Add New Model", "Edit Existing Model"])

with tab1:
    st.title("--Dapol Inventory Entry--")
    st.markdown(
        "Enter new model details below to ingest data into the **Bronze Layer**."
    )

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

with tab2:
    st.title("--Edit Existing Model--")

    engine = get_engine()

    with engine.connect() as conn:
        models_query = text(
            "SELECT id, name, dapol_product_code FROM bronze.raw_models ORDER BY name"
        )
        models_result = conn.execute(models_query)
        models_list = [(row[0], f"{row[1]} ({row[2]})") for row in models_result]

    if models_list:
        selected_model = st.selectbox(
            "Select Model to Edit:",
            options=[None] + models_list,
            format_func=lambda x: "Choose a model..." if x is None else x[1],
        )

        if selected_model:
            model_id = selected_model[0]

            with engine.connect() as conn:
                fetch_query = text(
                    "SELECT * FROM bronze.raw_models WHERE id = :model_id"
                )
                result = conn.execute(fetch_query, {"model_id": model_id})
                current_data = (
                    result.fetchone()._asdict() if result.rowcount > 0 else {}
                )

            if current_data:
                with st.form("model_edit", clear_on_submit=False):
                    col1, col2 = st.columns(2)

                    with col1:
                        name = st.text_input(
                            "Model Name", value=current_data.get("name", "")
                        )
                        prod_code = st.text_input(
                            "Dapol Product Code",
                            value=current_data.get("dapol_product_code", ""),
                        )
                        type_ = st.text_input(
                            "Model Type", value=current_data.get("type", "")
                        )
                        livery = st.text_input(
                            "Livery Company",
                            value=current_data.get("livery_company", ""),
                        )
                        running = st.text_input(
                            "Running Number",
                            value=current_data.get("running_number", ""),
                        )

                    with col2:
                        scale = st.text_input(
                            "Scale", value=current_data.get("scale", "")
                        )
                        coupling = st.text_input(
                            "Coupling Type", value=current_data.get("coupling_type", "")
                        )
                        dcc = st.text_input(
                            "DCC Status", value=current_data.get("dcc_status", "")
                        )
                        edition = st.text_input(
                            "Limited Edition Number",
                            value=current_data.get("limited_edition_no", ""),
                        )

                    description = st.text_area(
                        "Description",
                        value=current_data.get("description", ""),
                        max_chars=200,
                    )

                    col3, col4 = st.columns(2)

                    with col3:
                        physical_condition = st.text_input(
                            "Physical Condition",
                            value=current_data.get("physical_condition", ""),
                        )
                        price = st.number_input(
                            "Estimated Value (£)",
                            min_value=0.0,
                            step=0.01,
                            value=float(current_data.get("estimated_value", 0.0)),
                        )

                    with col4:
                        box_condition = st.text_input(
                            "Box Condition", value=current_data.get("box_condition", "")
                        )
                        min_acceptable_price = st.number_input(
                            "Min Acceptable Price (£)",
                            min_value=0.0,
                            step=0.01,
                            value=float(current_data.get("min_acceptable_price", 0.0)),
                        )

                    col5, col6 = st.columns(2)

                    with col5:
                        update_submitted = st.form_submit_button(
                            "Update Model", type="primary"
                        )

                    with col6:
                        delete_submitted = st.form_submit_button(
                            "Delete Model", type="secondary"
                        )

                    if update_submitted:
                        try:
                            update_query = text(
                                """
                                UPDATE bronze.raw_models SET
                                    name = :name,
                                    dapol_product_code = :prod_code,
                                    type = :type,
                                    description = :desc,
                                    livery_company = :livery,
                                    running_number = :running,
                                    limited_edition_no = :edition,
                                    scale = :scale,
                                    coupling_type = :coupling,
                                    dcc_status = :dcc,
                                    physical_condition = :phys,
                                    box_condition = :box,
                                    estimated_value = :est_val,
                                    min_acceptable_price = :min_val,
                                    updated_at = :updated
                                WHERE id = :model_id
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
                                "scale": scale,
                                "coupling": coupling,
                                "dcc": dcc,
                                "phys": physical_condition,
                                "box": box_condition,
                                "est_val": price,
                                "min_val": min_acceptable_price,
                                "updated": datetime.now(),
                                "model_id": model_id,
                            }

                            with engine.begin() as conn:
                                conn.execute(update_query, params)

                                st.success(f"Successfully updated '{name}'!")
                                st.rerun()

                            pass

                        except Exception as e:
                            st.error(f"Error updating model: {e}")

                    if delete_submitted:
                        try:
                            delete_query = text(
                                "DELETE FROM bronze.raw_models WHERE id = :model_id"
                            )

                            with engine.begin() as conn:
                                conn.execute(delete_query, {"model_id": model_id})

                            st.success(
                                f"Successfully deleted '{current_data.get('name', '')}'!"
                            )
                            st.rerun()

                            pass

                        except Exception as e:
                            st.error(f"Error deleting model: {e}")

    else:
        st.info("No models found in the database. Please add a model first.")
