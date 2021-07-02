import pandas as pd
import streamlit as st

@st.cache
def load_dataframe(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

    columns = list(df.columns)
    columns.append(None)

    return df, columns