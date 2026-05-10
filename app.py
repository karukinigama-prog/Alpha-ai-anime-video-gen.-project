import streamlit as st
import os
import time
from PIL import Image

# ── PAGE CONFIGURATION ──────────────────────
st.set_page_config(page_title="CODE-ANIMATION AI", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for "Cyber Void" look
st.markdown("""
    <style>
    .stApp { background-color: #05070F; }
    h1, h2, h3, p { color: #00F5FF !important; font-family: 'Courier New', monospace; }
    .stButton>button {
        width: 100%;
        border: 2px solid #9D00FF;
        background-color: #0A0D1A;
        color: white;
        transition: 0.3s;
    }
    .stButton>button:hover { border-color: #00F5FF; color: #00F5FF; }
    .css-1n76uvr { background-color: #0A0D1A; border: 1px solid #1A2A4A; }
    </style>
    """, unsafe_allow_html=True)

# ── SIDEBAR & CONTROLS ──────────────────────
with st.sidebar:
    st.title("⬡ CONTROLS")
    speed = st.slider("SPEED", 0.1, 5.0, 1.0)
    quality = st.select_slider("QUALITY", options=["LOW", "MID", "HIGH", "ULTRA"])
    st.info("මෙම Settings ඇනිමේෂන් එකේ Render එකට බලපානු ඇත.")

# ── MAIN UI ─────────────────────────────────
st.title("⬡ CYBER VOID - AI ANIMATION STREAM")
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("◈ INPUT PROMPT")
    # මෙතැනදී පරිශීලකයාට අවශ්‍ය දේ ලිවිය හැකියි
    user_prompt = st.text_area("ඇනිමේෂන් එකට අවශ්‍ය විස්තරය (Prompt) මෙතැන ලියන්න:", 
                                placeholder="උදා: Glowing neon sphere with orbital particles in 3D space...",
                                height=200)
    
    run_btn = st.button("🚀 GENERATE ANIMATION")
    
    if run_btn:
        st.write("🔄 ඇනිමේෂන් එක සකසමින් පවතී...")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            progress_bar.progress(percent_complete + 1)
        st.success("✅ සූදානම්!")

with col2:
    st.subheader("◈ LIVE STREAM PREVIEW")
    
    # ඇනිමේෂන් එක වෙබ් එකේ පෙන්වීම
    # Cloud එකේදී Ursina Window එක පෙන්වීමට නොහැකි නිසා අපි මෙතැනදී
    # placeholder එකක් භාවිතා කරමු. සැබෑ streaming සඳහා WebRTC භාවිතා කළ හැක.
    
    if run_btn:
        # මෙහිදී ඇනිමේෂන් එක Live Stream එකක් ලෙස පෙන්වීමට කේතය ක්‍රියාත්මක වේ
        st.video("https://www.w3schools.com/html/mov_bbb.mp4") # උදාහරණ වීඩියෝවක් (මෙතැනට ඔබේ Stream එක එනු ඇත)
        st.caption("AI විසින් ජනනය කරන ලද සජීවී ඇනිමේෂන් එක")
    else:
        # Placeholder Image
        st.image("https://img.freepik.com/free-vector/cyber-punk-futuristic-background_23-2148419161.jpg", 
                 caption="Prompt එක ලබා දී Run කරන්න.", use_column_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>CODE - ANIMATION v2.0 | Powered by Ursina & Streamlit</p>", unsafe_allow_html=True)
