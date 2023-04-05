import streamlit as st
from streamlit_option_menu import option_menu
from st_pages import Page, show_pages, add_page_title
from streamlit_folium import folium_static, st_folium
import folium
import pandas as pd

#Display all rows
pd.set_option('display.max_rows', 500)

pd.set_option('display.max_columns', None)

#Streamlit
st.set_page_config(page_title="WG Gesucht Analysis", layout="wide", initial_sidebar_state="expanded", menu_items={
    'Get Help': 'https://www.extremelycoolapp.com/help',
    'Report a bug': "https://www.extremelycoolapp.com/bug",
    'About': "# This is a header. This is an *extremely* cool app!"
})
st.markdown("<h1 style='text-align: center; color: orange;'>Property Analysis</h1>", unsafe_allow_html=True)

#Pages
page_real_estate_general_dashboard = "wggesucht.py"
page_maps = "pages/maps.py"
#page_payments = "/Users/christianheins/Documents/Coding/Projects/WGGesucht/pages/wggesucht3.py"

show_pages(
    [
        Page(page_real_estate_general_dashboard, "General Dashboard", "🏠"),
        Page(page_maps, "Other Dashboard", "🏠"),
    ]
)

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stHeader"] {
                background-image: url(https://www.lautgegennazis.de/wp-content/uploads/2016/10/WG_Banner.jpg);
                background-repeat: no-repeat;
                background-position: 62%;
                background-size: contain;
                padding-top: 100px;
            }
            [data-testid="stSidebarNav"] {
                background-image: url(https://play-lh.googleusercontent.com/FMudTGzgSiUN0ebC3gG5WkSBGn_xGA3M5FDs73F6G8Eam_pLhckoTbO53tMalltHKxw);
                background-repeat: no-repeat;
                background-size: contain;
                background-position: 50% 0%;
                padding-top: 80px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Pages";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()



