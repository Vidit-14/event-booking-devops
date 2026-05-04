import streamlit as st
import json
import os

# Set path relative to the script
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Must be the first Streamlit command
st.set_page_config(page_title="RC-SPIT Events", page_icon="🔥", layout="wide")

# Injecting some custom CSS for a cleaner hero section
st.markdown("""
    <style>
    .hero-text {
        font-size: 3.5rem !important;
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

# Hero Section
st.markdown('<p class="hero-text">🚀 Campus Event Hub</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-hero">The official portal. Secure your spot before they sell out.</p>', unsafe_allow_html=True)
st.divider()

data = load_data()

# Event Feed
st.subheader("🔥 Trending on Campus")
st.write("") # Spacer

for event in data['events']:
    # Using Streamlit 1.30+ native container borders for a 'Card' look
    with st.container(border=True): 
        col1, col2 = st.columns([2.5, 1.5])
        
        with col1:
            st.markdown(f"## {event['name']}")
            st.markdown(f"**📅 {event['date']}**")
            st.write(event['description'])
            
        with col2:
            available = event['capacity'] - event['booked']
            fill_percentage = event['booked'] / event['capacity']
            
            # Dynamic Status Badges
            if available == 0:
                st.error("🚨 SOLD OUT")
            elif fill_percentage > 0.8:
                st.warning(f"⚠️ Only {available} left! Moving fast.")
            else:
                st.success(f"✅ {available} Tickets Available")
            
            # Visual Progress Bar
            st.progress(fill_percentage, text=f"{event['booked']} / {event['capacity']} Booked")
            
            st.write("") # Spacer
            
            # Direct deep-link to the booking page
            if available > 0:
                st.page_link("pages/1_Ticket_Booking.py", label="Get Tickets", icon="🎫")