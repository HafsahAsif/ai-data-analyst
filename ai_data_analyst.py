import streamlit as st
import pandas as pd

st.title("AI Data Analyst 🚀")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    st.success("File loaded successfully!")
