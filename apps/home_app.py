import os
import streamlit as st
from hydralit import HydraHeadApp


class HomeApp(HydraHeadApp):

    def __init__(self, title='7blue Mailer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        try:
            # Display content here
            st.title("Welcome to 7blue Mailer!")
            st.markdown("""
            7blue Mailer is a powerful email marketing platform designed to help you create, send, and track your email campaigns with ease.
            """)

            st.header("Key Features:")
            st.markdown("""
            - **Intuitive Interface:** Our user-friendly interface makes it easy to design beautiful emails.
            - **Advanced Analytics:** Track the performance of your campaigns with detailed analytics.
            - **Segmentation:** Target your audience with precision by creating custom segments.
            - **Automation:** Automate your email campaigns to save time and increase efficiency.
            - **Responsive Design:** Ensure your emails look great on any device with responsive design.
            """)

            st.header("Get Started:")
            st.markdown("""
            Ready to get started? Sign up for an account or log in to access all the features of 7blue Mailer.
            """)

            st.image(os.path.join(".","resources","mailer_image.png"), width=500)
            
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"), width=100)
            st.error('An error has occurred. Please try again later.')
            st.error('Error details: {}'.format(e))
