import os
import streamlit as st
from hydralit import HydraHeadApp


class HomeApp(HydraHeadApp):

    def __init__(self, title = '7blue Mailer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):

        try:
            pass            
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))





