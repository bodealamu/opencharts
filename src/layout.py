import streamlit as st
from src.graph_controls import graph_controls
from src.utility import load_dataframe
from streamlit.components.v1 import iframe


def fixed_content():
    """
    Contains fixed content visible across different links
    :return:
    """
    st.sidebar.subheader('Maintenance')
    st.sidebar.write("This app is open source and maintained by Olabode Alamu, "
                     "if you would like to contribute to the code, please do a pull request.")

    #st.sidebar.subheader("Sever costs")
    # st.sidebar.write("Sever costs for this app is community funded, if you would like to donate please use link below.")
    # st.sidebar.write('https://www.buymeacoffee.com/olabodealamu')


def views(link):
    """
    Helper function for directing users to various pages.
    :param link: str, option selected from the radio button
    :return:
    """
    if link == 'Home':
        st.header("Welcome to OpenCharts")
        st.write("OpenCharts is an open source and community funded  web tool "
                 "for creating beautiful charts from data and "
                 "exporting those charts to different formats. ")
        st.subheader("Getting started")
        st.markdown("To create charts, upload your data, select a theme,"
                    "select a chart type,"
                    "set the chart options and download the chart.")
        st.subheader("Data safety and security")
        st.write("The data you upload is safe and is never stored anywhere.")
        # st.write('../logo.jpg')
        st.sidebar.subheader('Settings')

        st.sidebar.subheader("Upload your data")
        uploaded_file = st.sidebar.file_uploader(label="Upload your csv or excel file here.",
                                                 accept_multiple_files=False,
                                                 type=['csv', 'xlsx'])

        fixed_content()
        if uploaded_file is not None:
            df, columns = load_dataframe(uploaded_file=uploaded_file)

            st.sidebar.subheader("Visualize your data")

            show_data = st.sidebar.checkbox(label='Show data')

            if show_data:
                try:
                    st.subheader("Data view")
                    number_of_rows = st.sidebar.number_input(label='Select number of rows', min_value=2)

                    st.dataframe(df.head(number_of_rows))
                except Exception as e:
                    print(e)

            st.sidebar.subheader("Theme selection")

            theme_selection = st.sidebar.selectbox(label="Select your themes",
                                                   options=['plotly', 'plotly_white',
                                                            'ggplot2',
                                                            'seaborn', 'simple_white'])
            st.sidebar.subheader("Chart selection")
            chart_type = st.sidebar.selectbox(label="Select your chart type.",
                                              options=['Scatter plots', 'Density contour',
                                                       'Sunburst','Pie Charts','Density heatmaps',
                                                       'Histogram', 'Box plots','Tree maps',
                                                       'Violin plots', ])  # 'Line plots',

            graph_controls(chart_type=chart_type, df=df, dropdown_options=columns, template=theme_selection)

    if link == 'About':
        st.header('About')
        st.write("OpenCharts is an open source and free data " "visualization web app built using Streamlit ")
        st.subheader('Contact me')
        st.write("You can contact Olabode Alamu on linkedin https://www.linkedin.com/in/olabode-alamu/")
        fixed_content()

    if link == 'Tutorial':
        st.header("Tutorial")
        fixed_content()
        tutorial_video = st.selectbox(label='I would like to learn how to create ',
                                      options=['Scatterplots', 'Boxplots', 'Violinplots',
                                               'Histogram', 'Density Contour Charts'])
        if tutorial_video == 'Scatterplots':
            iframe(width=800,height=450,  src="https://www.youtube.com/embed/e_V_GwWjzH8")

        if tutorial_video == "Boxplots":
            iframe(width=800, height=450, src="https://www.youtube.com/embed/Q3fOS6hbi-8")

        if tutorial_video == 'Violinplots':
            iframe(width=800, height=450, src="https://www.youtube.com/embed/mjnsKF1I72g")

        if tutorial_video == 'Density Contour Charts':
            iframe(width=800, height=450, src="https://www.youtube.com/embed/C3tDr6T9hNY")






