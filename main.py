import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
    st.title("welcome to my first steamlit")

with dataset:
    st.header("here is my data")
    st.text("this is the text of my data")

    my_data = pd.read_csv("data.csv")
    st.write(my_data.head())

with features:
    st.header("this is the features of my app")
    st.text("this is the text of my data features")
