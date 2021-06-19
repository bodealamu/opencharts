import streamlit as st
import plotly.express as px
import pandas as pd


st.title("OpenCharts")
st.markdown("#### A tool used for creating data visualization apps without code.")

st.sidebar.subheader('Chart settings')

uploaded_file = st.sidebar.file_uploader(label="Upload your file here.",
                                         accept_multiple_files=False,
                                         type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

    columns = df.columns
chart_type = st.sidebar.selectbox(label="Select your chart type.",
                     options=['Scatter plots','Line plots', 'Histogram', 'Box plots', 'Violin plots', ])

print(chart_type)

if chart_type == 'Scatter plots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=columns)
        y_values = st.sidebar.selectbox('Y axis', options=columns)
        color_value = st.sidebar.selectbox("Color", options=columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values, color=color_value)
        # display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)