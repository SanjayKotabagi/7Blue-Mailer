import time
from typing import Dict
import streamlit as st
from hydralit import HydraHeadApp



class LoginApp(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self) -> None:
        st.markdown("<h1 style='text-align: center;'>7blue Mailer</h1>", unsafe_allow_html=True)
        c1,c2,c3, = st.columns([2,2,2])
        form_data = self._create_login_form(c2)
        pretty_btn = """
        <style>
        div[class="row-widget stButton"] > button {
            width: 100%;
        }
        </style>
        <br><br>
        """
        c2.markdown(pretty_btn,unsafe_allow_html=True)

        if form_data['submitted']:
            self._do_login(form_data, c2)


    def _create_login_form(self, parent_container) -> Dict:

        login_form = parent_container.form(key="login_form")

        form_state = {}
        form_state['username'] = login_form.text_input('Username')
        form_state['password'] = login_form.text_input('Password',type="password")
        form_state['submitted'] = login_form.form_submit_button('Login')

        if parent_container.button('Sign Up',key='signupbtn'):
            self.set_access(-1, 'guest')
            self.do_redirect()
        return form_state


    def _do_login(self, form_data, msg_container) -> None:
        access_level = self._check_login(form_data)
        if access_level > 0:
            form_data['access_level'] = 1
            msg_container.success(f"✔️ Login success")
            with st.spinner("🤓 now redirecting to application...."):
                time.sleep(1)
                self.set_access(form_data['access_level'], form_data['username'],cache_access=True)
                self.do_redirect()
        else:
            self.session_state.allow_access = 0
            self.session_state.current_user = None

            msg_container.error(f"❌ Login unsuccessful, 😕 please check your username and password and try again.")

    def _check_login(self, login_data) -> int:
        if login_data['username'] == 'joe' and login_data['password'] == 'joe':
            return 1
        else:
            return 0