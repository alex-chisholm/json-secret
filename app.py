import streamlit as st
import os
import json

st.set_page_config(page_title="Fake Credential Viewer", layout="wide")
st.title("🔐 Fake Credential Viewer")

# Read credential from environment variable
cred_str = os.getenv("FAKE_CREDENTIAL_JSON")

if cred_str is None:
    st.error("❌ Environment variable `FAKE_CREDENTIAL_JSON` not found.")
else:
    try:
        cred = json.loads(cred_str)
        st.success("✅ Credential loaded successfully!")
        st.subheader("📋 Credential Contents")

        for key, value in cred.items():
            # Display long strings (like keys) in a text area
            if isinstance(value, str) and len(value) > 100:
                st.text_area(key, value, height=100)
            else:
                st.text_input(key, value, disabled=True)
    except json.JSONDecodeError:
        st.error("⚠️ Failed to parse JSON credential. Please check the format.")
