import streamlit as st
from graph_controls import graph_controls
from utility import load_dataframe


# change max message size which can be sent via websocket
st.server.server_util.MESSAGE_SIZE_LIMIT = 300 * 1e6


st.header("Welcome to OpenCharts")
st.write("Beautiful visualization tools should be free and accessible to all.")
st.write('Upload your csv or excel file to get started.')

st.subheader('About')
st.write("OpenCharts is an open source and free data " "visualization web app built using Streamlit " )

st.sidebar.subheader('Maintenance')
st.sidebar.write("This app is open source and maintained by Olabode Alamu, "
                 "if you would like to contribute to the code, please do a pull request.")

st.sidebar.subheader("Sever costs")
st.sidebar.write("Sever costs for this app is community funded, if you would like to donate please use link below.")
st.sidebar.write('https://www.buymeacoffee.com/olabodealamu')

st.sidebar.subheader('Settings')

st.sidebar.subheader("Upload your data")
uploaded_file = st.sidebar.file_uploader(label="Upload your csv or excel file here.",
                                         accept_multiple_files=False,
                                         type=['csv', 'xlsx'])

if uploaded_file is not None:
    df, columns = load_dataframe(uploaded_file=uploaded_file)

    show_data = st.sidebar.checkbox(label='Show data')

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
    st.write("'The data you upload is safe and is never stored anywhere.")

    st.subheader('Contact me')
    st.write("You can contact me on linkedin https://www.linkedin.com/in/olabode-alamu/")




