import streamlit as st
import time

st.set_page_config(
    page_title="SentinelX",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ SentinelX")
st.subheader("Women Safety & Emergency AI App")

st.markdown("---")

st.write("AI-powered emergency protection system.")

# ----------------------------
# Fake Call
# ----------------------------

if st.button("📞 Generate Fake Call"):

    st.warning("Incoming call in 5 seconds...")

    time.sleep(5)

    st.success("📱 MOM CALLING...")

# ----------------------------
# SOS
# ----------------------------

if st.button("🚨 Emergency SOS"):

    st.error("Emergency alert activated!")

    st.write("📍 Live location shared")
    st.write("📨 Emergency contacts notified")
    st.write("🎙️ Emergency recording started")

# ----------------------------
# Danger Analysis
# ----------------------------

situation = st.text_area(
    "Describe emergency situation"
)

if st.button("🧠 Analyze Danger"):

    if "help" in situation.lower():

        st.error("⚠️ HIGH RISK DETECTED")

        st.write("""
        Recommended Actions:
        - Move to crowded area
        - Contact trusted person
        - Call emergency services
        - Share live location
        """)

    else:

        st.success("Situation appears safer.")

st.markdown("---")
st.caption("Built for Hackathon 🚀")
