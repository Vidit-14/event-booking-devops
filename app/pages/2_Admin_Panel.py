import streamlit as st
import json
import pandas as pd
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data.json')

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

st.set_page_config(page_title="Admin Dashboard", page_icon="🔒")
st.title("🔒 Admin Dashboard")

# Simple hardcoded password for lab demonstration
password = st.text_input("Enter Admin Password", type="password")

if password == "devops123":
    data = load_data()
    st.success("Access Granted")
    
    st.subheader("Deployment Architecture")
    st.info("Status: Running on Local Kubernetes Cluster via Docker Desktop")
    
    st.subheader("Recent Registrations")
    if data['bookings']:
        df = pd.DataFrame(data['bookings'])
        st.dataframe(df, use_container_width=True)
    else:
        st.write("No bookings yet.")
elif password:
    st.error("Incorrect Password")