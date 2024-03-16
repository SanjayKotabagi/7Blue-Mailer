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
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        use_banner_images=[None,None,None,None,None], 
        banner_spacing=[5,30,60,30,5],
        use_navbar=True, 
        navbar_sticky=True,
        navbar_animation=True,
        navbar_theme=over_theme,
        use_cookie_cache=False    
    ),

    app.add_app("Signup", icon="🛰️", app=apps.SignUpApp(title='Signup'), is_unsecure=True)
    app.add_app("Login", apps.LoginApp(title='Login'),is_login=True) 

    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)
    
    app.add_loader_app(apps.MyLoadingApp(delay=0))
   
    user_access_level, username = app.check_access()

   
    
    complex_nav = {
            'Home': ['Home'],
        }

  
    app.run(complex_nav)

