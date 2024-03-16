from hydralit import HydraApp
import hydralit_components as hc
import apps
import streamlit as st

if __name__ == '__main__':

    over_theme = {'txc_inactive': '#FFFFFF'}
    app = HydraApp(
        title='7blue Mailer',
        favicon="🐙",
        hide_streamlit_markers=True,
        use_banner_images=[None,None,None,None,None], 
        banner_spacing=[5,30,60,30,5],
        use_navbar=True, 
        use_cookie_cache=True,
        navbar_mode='sticky',
        navbar_sticky=True,
        navbar_animation=True,
        navbar_theme=over_theme,
    )
    st.markdown("""
    <style>
    .hydra-header {
    margin-top: -100;
    }
    </style>
    """,unsafe_allow_html=True)
    app.add_app("Signup", icon="🛰️", app=apps.SignUpApp(title='Signup'), is_unsecure=True)
    app.add_app("Login", apps.LoginApp(title='Login'),is_login=True) 

    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)
    app.add_app("About", icon="ℹ️", app=apps.AboutApp(title='About'))
    app.add_app("Features", icon="🔧", app=apps.FeaturesApp(title='Features'))
    app.add_app("Pricing", icon="💰", app=apps.PricingApp(title='Pricing'))
    app.add_app("Dashboard", icon="📊", app=apps.DashboardApp(title='Dashboard'))
    app.add_app("Campaign Creation", icon="🚀", app=apps.CampaignCreationApp(title='Campaign Creation'))
    app.add_app("Analytics", icon="📈", app=apps.AnalyticsApp(title='Analytics'))
    app.add_app("Settings", icon="⚙️", app=apps.SettingsApp(title='Settings'))
    app.add_app("Help", icon="❓", app=apps.HelpApp(title='Help'))
   
    user_access_level, username = app.check_access()

    complex_nav = {
    'Home': ['Home'],
    'About': ['About'],
    'Features': ['Features'],
    'Pricing': ['Pricing'],
    'Dashboard': ['Dashboard'],
    'Campaign Creation': ['Campaign Creation'],
    'Analytics': ['Analytics'],
    'Settings': ['Settings'],
    'Help': ['Help']
    }

    st.markdown(
        """
        <style>
        div[data-stale="false"] > iframe[title="hydralit_components.NavBar.nav_bar"] {
            position: fixed;
            width: 100%;
            z-index: 99;
            box-sizing: border-box;
            top: 0;
            left: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    app.run(complex_nav)
