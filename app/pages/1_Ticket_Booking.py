import streamlit as st
import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data.json')

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

st.set_page_config(page_title="Book Tickets", page_icon="🎫", layout="wide")

# Custom CSS for the clean header
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

st.markdown('<p class="hero-text">🎫 Secure Your Spot</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-hero">Lock in your tickets before they drop to zero.</p>', unsafe_allow_html=True)
st.divider()

data = load_data()
event_names = [e['name'] for e in data['events']]

# Select event outside the form so the UI reacts instantly
selected_event = st.selectbox("🎯 Select an Event", event_names)

# Find the current event data
current_event = next((e for e in data['events'] if e['name'] == selected_event), None)
available = current_event['capacity'] - current_event['booked']
fill_percentage = current_event['booked'] / current_event['capacity']

col1, col2 = st.columns([2, 1.5])

with col2:
    # Reactive Live Capacity Board
    with st.container(border=True):
        st.subheader("📊 Live Capacity")
        st.write(f"**{current_event['name']}**")
        
        if available == 0:
            st.error("🚨 Status: SOLD OUT")
        elif fill_percentage > 0.8:
            st.warning(f"⚠️ Status: Almost Gone ({available} left)")
        else:
            st.success(f"✅ Status: Available ({available} left)")
            
        st.progress(fill_percentage)

with col1:
    # Booking Form
    with st.container(border=True):
        st.subheader("📝 Guest Registration")
        with st.form("booking_form", border=False):
            name = st.text_input("Full Name", placeholder="e.g., John Doe")
            student_id = st.text_input("Student ID", placeholder="Enter your college ID")
            
            st.write("") # Spacer
            
            # Disable submit if sold out
            if available > 0:
                submit = st.form_submit_button("Confirm Booking 🚀", use_container_width=True)
            else:
                st.error("Registration closed for this event.")
                submit = st.form_submit_button("Waitlist (Coming Soon)", disabled=True, use_container_width=True)

            if submit and available > 0:
                if name and student_id:
                    # Update local data
                    current_event['booked'] += 1
                    data['bookings'].append({
                        "name": name,
                        "student_id": student_id,
                        "event": selected_event
                    })
                    save_data(data)
                    
                    st.success(f"Ticket confirmed for {name}! See you at {selected_event}.")
                    st.balloons() # Visual flair for successful booking
                else:
                    st.warning("⚠️ Please fill in all details.")