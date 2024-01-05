import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("The Best Company")
content1='''
Hello. This is an amazing company which will 
help you till the last possible efforts. 
'''
st.write(content1)
st.subheader("Our Team")

df=pandas.read_csv("data.csv", sep=",")
col1, emp_col1, col2, emp_col2, col3= st.columns([1,0.5,1,0.5,1])

with col1:
    for i, row in df[:4].iterrows():
        name=row["first name"]+" " +row["last name"]
        st.subheader(name.title())
        st.write(row["role"])
        st.image("Images/"+row["image"])

with col2:
    for i, row in df[4:8].iterrows():
        name=row["first name"]+" " +row["last name"]
        st.subheader(name.title())
        st.write(row["role"])
        st.image("Images/"+row["image"])

with col3:
    for i, row in df[8:].iterrows():
        name=row["first name"]+" " +row["last name"]
        st.subheader(name.title())
        st.write(row["role"])
        st.image("Images/"+row["image"])