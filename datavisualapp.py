import streamlit as st
import pandas as pd
from graph_controls import graph_controls


st.header("Welcome to OpenCharts")
st.write("Beautiful visualization should be free and accessible to all.")
st.write('Upload your csv or excel file to get started.')

st.subheader('About')
st.write("OpenCharts is an open source and free data "
                 "visualization web app built using Streamlit "
                 "and Plotly." )

st.sidebar.subheader('Maintenance')
st.sidebar.write("This app is maintained by Olabode Alamu, "
                 "if you would like to contribute to the code, please do a pull request.")

st.sidebar.subheader("Buy me a beer / server plan")
st.sidebar.write("This app is deployed on Digital ocean and is non-profit. "
                 "If you would like to support this cause with server costs, feel free to use the link below.")
st.sidebar.write('https://www.buymeacoffee.com/olabodealamu')

st.sidebar.subheader('Settings')
# st.sidebar.markdown(### Welcome to OpenCharts, an open source data visualization web application. Contributors to the code are welcome and encouraged)

st.sidebar.subheader("Upload your data")
uploaded_file = st.sidebar.file_uploader(label="Upload your csv or excel file here.",
                                         accept_multiple_files=False,
                                         type=['csv', 'xlsx'])


global df
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

    columns = list(df.columns)
    columns.append(None)

    show_data = st.sidebar.checkbox(label='SHow data')

    if show_data:
        number_of_rows = st.sidebar.number_input(label='Select number of rows',min_value=2)

        st.dataframe(df.head(number_of_rows))

    st.sidebar.subheader("Theme selection")

    theme_selection = st.sidebar.selectbox(label="Select your themes",
                                           options=['plotly', 'plotly_white',
                                                    'ggplot2',
                                                    'seaborn', 'simple_white'])
    st.sidebar.subheader("Chart selection")
    chart_type = st.sidebar.selectbox(label="Select your chart type.",
                                      options=['Scatter plots','Density contour',
                                               'Histogram','Box plots', 'Violin plots', ]) #'Line plots',

    graph_controls(chart_type=chart_type, df=df, dropdown_options=columns, template=theme_selection)

else:
    st.subheader("Data safety and security")
    st.write("'The data you upload is safe and does not "
             "leave your computer and is never stored anywhere.")

    st.subheader('Contact me')
    st.write("You can contact me on linkedin https://www.linkedin.com/in/olabode-alamu/")




