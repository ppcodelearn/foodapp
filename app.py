import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

app = MultiApp()

st.markdown("""
# Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# # horizontal menu
# selected2 = option_menu(None, ["Home", "Upload", "Tasks"], 
#     icons=['house', 'cloud-upload', "list-task"], 
#     menu_icon="cast", default_index=0, orientation="horizontal")


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Upload", data.app)
app.add_app("Task", model.app)

# The main app
app.run()
