import streamlit as st
from sqlalchemy import create_engine


def get_engine():
    db_url = st.secrets["connections"]["postgresql"]["url"]
    return create_engine(db_url)
