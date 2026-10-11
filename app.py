import streamlit as st

st.set_page_config(page_title="GenAI Deployment Hub", page_icon="🚀", layout="centered")

st.title("🚀 GenAI Application Deployment Portal")
st.write("Welcome! This application demonstrates the successful deployment of a Generative AI web interface.")

user_name = st.text_input("Enter your name:")
if user_name:
    st.success(f"Hello, {user_name}! Your GenAI application is live and running successfully.")

st.info("This app serves as a robust endpoint for cloud demonstration and production validation.")