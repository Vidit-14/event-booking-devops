import streamlit as st
import json
import pandas as pd
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data.json')

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

st.set_page_config(page_title="Admin Dashboard", page_icon="🔐", layout="wide")

st.markdown("""
    <style>
    .hero-text {
        font-size: 3rem !important;
        font-weight: 800 !important;
        margin-bottom: 0px !important;
        letter-spacing: -1.5px;
    }
    .sub-hero {
        color: #888888;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="hero-text">🔐 Admin Command Center</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-hero">Restricted access. Manage bookings and monitor cluster health.</p>', unsafe_allow_html=True)
st.divider()

# Auth Box
auth_container = st.container(border=True)
with auth_container:
    password = st.text_input("Enter Root Password", type="password", placeholder="Password...")

if password == "devops123":
    data = load_data()
    st.success("Authentication Successful. Welcome back.")
    
    # Top-Level Metrics
    st.write("### 📈 Live Operations")
    col1, col2, col3 = st.columns(3)
    
    total_events = len(data.get('events', []))
    total_bookings = len(data.get('bookings', []))
    
    with col1:
        st.metric(label="Active Events", value=total_events)
    with col2:
        st.metric(label="Total Tickets Issued", value=total_bookings)
    with col3:
        st.metric(label="Cluster Status", value="Healthy", delta="K8s Online")
        
    st.write("") # Spacer

    # Architecture & Data Tables
    col_arch, col_data = st.columns([1, 2])
    
    with col_arch:
        with st.container(border=True):
            st.markdown("#### ⚙️ Architecture")
            st.info("🌐 **Frontend:** Streamlit\n\n🐳 **Container:** Docker\n\n☸️ **Orchestrator:** Kubernetes\n\n☁️ **Registry:** Docker Hub")
    
    with col_data:
        with st.container(border=True):
            st.markdown("#### 🎫 Recent Registrations")
            if data.get('bookings'):
                df = pd.DataFrame(data['bookings'])
                # Using hide_index to make the table look much cleaner
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.write("No bookings recorded yet.")
                
elif password:
    st.error("🚨 Access Denied: Incorrect credentials.")