import streamlit as st
import sys
import contextlib
import streamlit.components.v1 as components
from io import StringIO
from feeds import get_latest_news
from llm_client import analyze_trends

st.set_page_config(page_title="PulseCheck AI", layout="wide", page_icon="📡")

def apply_themes():
    st.markdown("""
    <style>
    /* Dark Slate Background */
    .stApp { background-color: #0f172a; color: #f8fafc; }
    
    /* Clean Sidebar */
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    
    /* Soft Mint Accents for Buttons */
    .stButton>button { 
        background-color: #10b981; color: white; border: none; 
        border-radius: 8px; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #059669; border: none; color: white; }
    
    /* Elegant Metric Cards */
    [data-testid="stMetric"] {
        background: #1e293b; border: 1px solid #334155; 
        padding: 15px; border-radius: 12px;
    }
    
    h1 { color: #10b981; font-weight: 800; text-align: left; }
    </style>
    """, unsafe_allow_html=True)

def st_lottie_safe(url, height=180):
    """Stable HTML-based Lottie player"""
    lottie_html = f"""
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <div style="display: flex; justify-content: center;">
            <lottie-player src="{url}" background="transparent" 
                           speed="1" style="width: {height}px; height: {height}px;" loop autoplay>
            </lottie-player>
        </div>
    """
    components.html(lottie_html, height=height)

class LogCapture:
    def __init__(self, placeholder):
        self.buffer = StringIO()
        self.placeholder = placeholder
    def write(self, data):
        self.buffer.write(data)
        self.placeholder.code(self.buffer.getvalue())
    def flush(self): pass

apply_themes()

with st.sidebar:
    st.title("📡 System Monitor")
    st.caption("v1.2.0 - Stable Build")
    st.divider()
    st.subheader("🖥️ Activity Logs")
    log_display = st.empty()

st.markdown("<h1>PulseCheck Intelligence</h1>", unsafe_allow_html=True)

cols = st.columns(3)
cols[0].metric("Engine", "Groq Llama 3")
cols[1].metric("Source", "Live RSS")
cols[2].metric("Status", "Operational")

if st.button("RUN SCAN"):
    log_capturer = LogCapture(log_display)
    sys.stdout = log_capturer
    
    try:
        st_lottie_safe("https://assets5.lottiefiles.com/packages/lf20_V9t630.json", height=120)
        
        news = get_latest_news()
        analysis = analyze_trends(news)
        
        st.divider()
        st.subheader("🔍 AI Analysis Report")
        
        if hasattr(st, "write_stream"):
            st.write_stream(iter(analysis.split(" ")))
        else:
            st.write(analysis)
            
    finally:
        sys.stdout = sys.__stdout__