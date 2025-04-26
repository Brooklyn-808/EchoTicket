import streamlit as st
import requests
import json
import os

def get_server_data():
    # Simulate fetching the dictionary from the API
    return {
        "1365519077786914877": {
            "key": "nuh uh",
            "open": False,
            "ticket-open-message": "Click the button to create a ticket!",
            "ticket-category": "Support",
            "ticket-channel": "ticket-",
            "ticket-message": "Hello {{user}}, a <@1365520086961619025> will be with you shortly. Please provide as much detail as possible on your problem.",
            "auto-rename": False,
            "user-close": False,
            "staff-id": 1365520086961619025,
            "whitelist": False,
            "role-id": 1365523762354585620,
            "ticket-transcribe": True,
            "transcript": 1365525180528594994
        }
    }

st.title("Edit Server Configurations")

# Form to edit servers.json
with st.form("edit_config_form"):
    st.subheader("Update Server Configuration")

    key = st.text_input("Key", placeholder="Enter the sevrer key")
    change_key = st.text_input("Change Key", placeholder="Enter the key to change")

    value_placeholder = "Enter the new value"
    if change_key == "key":
        value = st.text_input("Value", placeholder=value_placeholder, disabled=True)
    elif change_key == "ticket-open-message":
        value = st.text_input("Value", placeholder=value_placeholder)
    elif change_key == "ticket-category":
        
        value = st.text_input("Value", placeholder=value_placeholder)
    elif change_key == "ticket-channel":
        
        value = st.text_input("Value", placeholder=value_placeholder)
    elif change_key == "ticket-message":
        
        value = st.text_input("Value", placeholder=value_placeholder)
    elif change_key == "auto-rename":
        
        value = st.selectbox("Value", options=[True, False])
    elif change_key == "user-close":
        
        value = st.selectbox("Value", options=[True, False])
    elif change_key == "staff-id":
        
        value = st.number_input("Value", value=0)
    elif change_key == "whitelist":
        
        value = st.selectbox("Value", options=[True, False])
    elif change_key == "role-id":
        
        value = st.number_input("Value", value=0)
    elif change_key == "ticket-transcribe":
        
        
        value = st.selectbox("Value", options=[True, False])
    elif change_key == "transcript":
        
        value = st.number_input("Value", value=0)
    else:
        value = st.text_input("Value", placeholder=value_placeholder)
    

    # Submit button
    submitted = st.form_submit_button("Update Configuration")

    if submitted:
        # Send POST request to the API endpoint
        api_url = "http://212.192.29.158:25200/update-config"  # Replace with the actual API URL
        payload = {
            "key": key,
            "change": change_key,
            "value": value
        }

        try:
            response = requests.post(api_url, data=payload)
            if response.status_code == 200:
                st.success("Configuration updated successfully!")
            elif response.status_code == 403:
                st.error("Unauthorized: Invalid key.")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
