import streamlit as st
from importer import import_data

# Import Data
df = import_data()

st.dataframe(df)
