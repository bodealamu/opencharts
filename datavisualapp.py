import streamlit as st
from src.layout import views

# change max message size which can be sent via websocket
st.server.server_util.MESSAGE_SIZE_LIMIT = 300 * 1e6

# navigation links
link = st.sidebar.radio(label='Links', options=['Home', 'About', 'Tutorial'])

views(link)

