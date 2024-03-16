import os
import streamlit as st
from hydralit import HydraHeadApp

class HelpApp(HydraHeadApp):

    def __init__(self, title='Help for 7blue Mailer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        try:
            st.title("Help for 7blue Mailer")

            st.markdown("""
            Welcome to the help page for 7blue Mailer! Here, you'll find useful resources and information to assist you in using our platform effectively.

            **Frequently Asked Questions (FAQs):**
            Have questions about how to use 7blue Mailer? Check out our [FAQs page](https://www.7bluemailer.com/faqs) for answers to common questions.

            **Getting Started Guide:**
            New to 7blue Mailer? Our [Getting Started Guide](https://www.7bluemailer.com/getting-started) provides step-by-step instructions to help you get up and running quickly.

            **Video Tutorials:**
            Prefer visual instructions? Watch our [video tutorials](https://www.7bluemailer.com/video-tutorials) for demonstrations of key features and functionalities.

            **Contact Support:**
            Need further assistance? Contact our support team at support@7bluemailer.com for personalized help and support.

            We're here to help you succeed with 7blue Mailer! If you have any questions or feedback, don't hesitate to reach out to us.
            """)

            st.image(os.path.join(".", "resources", "help_image.png"), width=500)
            
        except Exception as e:
            st.image(os.path.join(".", "resources", "failure.png"), width=100)
            st.error('An error has occurred. Please try again later.')
            st.error('Error details: {}'.format(e))
