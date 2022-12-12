import streamlit as st
from importer import import_data

df = import_data()
st.dataframe(df)
