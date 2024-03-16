import os
import streamlit as st
from hydralit import HydraHeadApp

class AboutApp(HydraHeadApp):

    def __init__(self, title='About 7blue Mailer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        try:
            st.title("About 7blue Mailer")

            st.markdown("""
            7blue Mailer is a powerful email marketing platform designed to streamline your email marketing efforts. 
            Whether you're a small business owner or a marketing professional, our platform provides all the tools 
            you need to create, send, and track your email campaigns with ease.

            **Key Features:**
            - **Intuitive Interface:** Our user-friendly interface makes it easy to design beautiful emails.
            - **Advanced Analytics:** Track the performance of your campaigns with detailed analytics.
            - **Segmentation:** Target your audience with precision by creating custom segments.
            - **Automation:** Automate your email campaigns to save time and increase efficiency.
            - **Responsive Design:** Ensure your emails look great on any device with responsive design.

            **Our Mission:**
            Our mission is to empower businesses of all sizes to succeed in their email marketing efforts. 
            We strive to provide innovative solutions that simplify the email marketing process and deliver 
            measurable results for our clients.

            **Contact Us:**
            Have questions or feedback? We'd love to hear from you! Contact our support team at support@7bluemailer.com.
            """)

            st.image(os.path.join(".", "resources", "mailer_logo.png"), width=300)
            
        except Exception as e:
            st.image(os.path.join(".", "resources", "failure.png"), width=100)
            st.error('An error has occurred. Please try again later.')
            st.error('Error details: {}'.format(e))
