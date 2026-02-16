import streamlit as st

PAGE_CONFIG = dict(
    page_title="Microeletrônica no Brasil",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

_CSS = """
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.1rem;
        opacity: 0.7;
        margin-top: -10px;
        margin-bottom: 30px;
    }
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        padding: 16px 20px;
    }
    div[data-testid="stMetric"] label,
    div[data-testid="stMetric"] div[data-testid="stMetricValue"],
    div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
        color: white !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        font-size: 1.8rem !important;
    }
    [data-testid="stSidebar"] [data-testid="stMarkdown"] p,
    [data-testid="stSidebar"] [data-testid="stMarkdown"] h2,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span {
        color: inherit !important;
    }
    hr {
        border: none;
        border-top: 2px solid rgba(128, 128, 128, 0.3);
        margin: 2rem 0;
    }
</style>
"""


def inject_css() -> None:
    """Inject custom CSS into the Streamlit page."""
    st.markdown(_CSS, unsafe_allow_html=True)
