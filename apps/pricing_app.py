import os
import streamlit as st
from hydralit import HydraHeadApp

class PricingApp(HydraHeadApp):

    def __init__(self, title='Pricing of 7blue Mailer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        try:
            st.title("Pricing of 7blue Mailer")

            # Pricing plans layout
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("""
                <div class="pricing-card">
                    <h2>Monthly Plan</h2>
                    <p class="price">₹300 per month</p>
                    <ul>
                        <li>Unlimited email campaigns</li>
                        <li>Advanced analytics</li>
                        <li>Segmentation tools</li>
                        <li>Automation features</li>
                        <li>Responsive design</li>
                        <li>Email template library</li>
                        <li>Integration with other platforms</li>
                        <li>Dedicated support</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown("""
                <div class="pricing-card">
                    <h2>Yearly Plan</h2>
                    <p class="price">₹3000 per year</p>
                    <p class="savings">Save ₹600</p>
                    <ul>
                        <li>All features included in the monthly plan</li>
                        <li>Save ₹600 with annual billing</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            # Custom CSS for styling
            st.markdown("""
            <style>
            .pricing-card {
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                margin-bottom: 20px;
            }
            .price {
                font-size: 24px;
                font-weight: bold;
                color: #333;
            }
            .savings {
                color: green;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin-bottom: 10px;
                color: #555;
            }
            </style>
            """,unsafe_allow_html=True)

            st.image(os.path.join(".", "resources", "pricing_image.png"), width=500)
            
        except Exception as e:
            st.image(os.path.join(".", "resources", "failure.png"), width=100)
            st.error('An error has occurred. Please try again later.')
            st.error('Error details: {}'.format(e))
