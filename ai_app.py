### ai web app
import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="AI ML Web App",
    layout="wide"
)

# Title
st.title("Data Science & Machine Learning Web Application")

st.write("Upload a CSV file to begin.")

# Upload file
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

# If file uploaded
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset loaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Rows and Columns")
    st.write(df.shape)

    st.subheader("Column Types")
    st.write(df.dtypes)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

else:
    st.info("Waiting for CSV upload...")