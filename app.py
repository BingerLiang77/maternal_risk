import streamlit as st

st.set_page_config(
    page_title="Maternal Health Dashboard",
    page_icon="🩺",
    layout="wide"
)

pages = {
    "Dashboard": [
        st.Page("pages/0_Home.py", title="Home"),
    ],
    "Explore": [
        st.Page("pages/1_Dataset_Overview.py", title="Population Distributions"),
        st.Page("pages/2_Distribution.py", title="Risk-Level Comparisons"),
        st.Page("pages/3_Correlation.py", title="Feature Correlations"),
    ],
}

pg = st.navigation(pages)
pg.run()