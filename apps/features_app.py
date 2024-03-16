import os
import streamlit as st
from hydralit import HydraHeadApp

class FeaturesApp(HydraHeadApp):

    def __init__(self, title='Features of 7blue Mailer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        try:
            st.title("Features of 7blue Mailer")

            st.markdown("""
            - **Intuitive Interface:** Our platform features an intuitive drag-and-drop interface that allows you to easily design beautiful and engaging email campaigns without any coding skills required.

            - **Advanced Analytics:** Track the performance of your email campaigns with detailed analytics including open rates, click-through rates, bounce rates, and more. Gain insights into your audience's behavior and optimize your campaigns for better results.

            - **Segmentation:** Target your audience with precision by creating custom segments based on demographics, behavior, and engagement history. Deliver personalized content to different segments of your audience for increased engagement and conversions.

            - **Automation:** Streamline your email marketing efforts with powerful automation features. Set up automated email sequences, drip campaigns, and autoresponders to deliver the right message to the right people at the right time.

            - **Responsive Design:** Ensure that your email campaigns look great on any device with responsive design. Our platform automatically adjusts the layout and formatting of your emails to ensure a consistent and optimized experience for your recipients.

            - **Template Library:** Choose from a variety of professionally designed email templates to kickstart your campaigns. Customize the templates to match your brand identity and create stunning emails in minutes.

            - **Integration:** Seamlessly integrate with other marketing tools and platforms to streamline your workflow. Connect 7blue Mailer with your CRM, e-commerce platform, or social media accounts for a more comprehensive marketing strategy.

            - **Support:** Our dedicated support team is here to help you every step of the way. Whether you have questions about using the platform or need assistance with your campaigns, we're always available to provide expert guidance and support.
            """)

            st.image(os.path.join(".", "resources", "features_image.png"), width=500)
            
        except Exception as e:
            st.image(os.path.join(".", "resources", "failure.png"), width=100)
            st.error('An error has occurred. Please try again later.')
            st.error('Error details: {}'.format(e))
