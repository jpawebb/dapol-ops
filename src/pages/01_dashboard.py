import streamlit as st
import pandas as pd

from db_connection import get_engine

# 1. Connect to Neon
engine = get_engine()

with engine.connect() as conn:

    # 2. Pull the "Gold" data created by dbt
    df = pd.read_sql("SELECT * FROM marts.dim_models", conn)

    # 3. Display High-Level Metrics
    st.title("🚂 DapolOps Executive Summary")

    col1, col2 = st.columns(2)
    col1.metric("Total Models", len(df))
    col2.metric("Total Value", f"£{df['estimated_value'].sum():,.2f}")

    # 4. Value by Model Type Chart
    st.subheader("Value by Model Type")
    st.bar_chart(data=df, x="model_subtype", y="estimated_value")

    # 5. Inventory Table
    st.subheader("Full Inventory")
    st.dataframe(df[["full_title", "model_type", "scale", "estimated_value"]])
