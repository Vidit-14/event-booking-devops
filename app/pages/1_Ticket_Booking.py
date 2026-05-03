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

st.set_page_config(page_title="Book a Ticket", page_icon="🎫")
st.title("🎫 Secure Your Spot")

data = load_data()
event_names = [e['name'] for e in data['events']]

with st.form("booking_form"):
    name = st.text_input("Full Name")
    student_id = st.text_input("Student ID")
    selected_event = st.selectbox("Select Event", event_names)
    submit = st.form_submit_button("Book Ticket")

    if submit:
        if name and student_id:
            for event in data['events']:
                if event['name'] == selected_event:
                    if event['booked'] < event['capacity']:
                        event['booked'] += 1
                        data['bookings'].append({
                            "name": name,
                            "student_id": student_id,
                            "event": selected_event
                        })
                        save_data(data)
                        st.success(f"Ticket confirmed for {name}! See you at {selected_event}.")
                    else:
                        st.error("Sorry, this event is sold out!")
        else:
            st.warning("Please fill in all details.")