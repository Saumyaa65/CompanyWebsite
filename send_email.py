import os

import streamlit as st
import os
import smtplib, ssl

def send_email(raw_message, email, topic):
    host="smtp.gmail.com"
    port=465
    username="keepstudying65"
    password="wpqydvljzykbfwsw"

    receiver="saumyaagarwal65@gmail.com"
    context=ssl.create_default_context()
    message=f"""\
Subject: New email from {email}
From: {email}
Topic: {topic}
{raw_message}
    """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

# to create requirements.txt, execute this command in terminal: pip freeze > requirements.txt