import streamlit as st
import json
import os

# Set path relative to the script
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

st.set_page_config(page_title="Campus Events", page_icon="🎟️", layout="wide")

st.title("🎟️ Campus Event Hub")
st.write("Welcome to the official portal. Check out upcoming events and secure your spot!")

data = load_data()

st.subheader("Upcoming Events")
for event in data['events']:
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {event['name']}")
            st.write(f"📅 **Date:** {event['date']}")
            st.write(event['description'])
        with col2:
            available = event['capacity'] - event['booked']
            st.metric(label="Tickets Left", value=available)
        st.divider()