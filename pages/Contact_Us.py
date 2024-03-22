import streamlit as st
import pandas
from send_email import send_email

options=pandas.read_csv("topics.csv")

with st.form(key="email"):
    email=st.text_input("Your email address")
    topic=st.selectbox("What do you wanna discuss?",
                       options=options)
    message=st.text_area("Text")
    button=st.form_submit_button()
    if button:
        send_email(message.encode('utf-8'), email, topic)
        st.info("Email sent successfully")