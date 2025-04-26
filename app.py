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
st.set_page_config(page_title="Server Configurations", page_icon="🗂️")
st.title("Edit Server Configurations")

# Form to edit servers.json
with st.form("edit_config_form"):
    st.subheader("Update Server Configuration")

    key = st.text_input("Key", placeholder="Enter the server key", help="The unique identifier for the server.")
    change_key = st.selectbox(
        "Change Key",
        options=[
            "ticket-open-message", "ticket-category", "ticket-channel", "ticket-message",
            "auto-rename", "user-close", "staff-id", "whitelist", "role-id", "ticket-transcribe", "transcript"
        ],
        help="Select the configuration key you want to update."
    )

    input_types = {
        "ticket-open-message": st.text_input,
        "ticket-category": st.text_input,
        "ticket-channel": st.text_input,
        "ticket-message": st.text_input,
        "auto-rename": st.selectbox,
        "user-close": st.selectbox,
        "staff-id": st.number_input,
        "whitelist": st.selectbox,
        "role-id": st.number_input,
        "ticket-transcribe": st.selectbox,
        "transcript": st.number_input
    }

    input_args = {
        "ticket-open-message": {"placeholder": "Enter the new message"},
        "ticket-category": {"placeholder": "Enter the new category"},
        "ticket-channel": {"placeholder": "Enter the new channel prefix"},
        "ticket-message": {"placeholder": "Enter the new ticket message"},
        "auto-rename": {"options": [True, False]},
        "user-close": {"options": [True, False]},
        "staff-id": {"value": 0},
        "whitelist": {"options": [True, False]},
        "role-id": {"value": 0},
        "ticket-transcribe": {"options": [True, False]},
        "transcript": {"value": 0}
    }
    if change_key.strip() != "":
        value = input_types[change_key]("Value", **input_args[change_key])

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
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                st.success("Configuration updated successfully!")
            elif response.status_code == 403:
                st.error("Unauthorized: Invalid key. Please check your server key.")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}. Please check your network connection and try again.")
