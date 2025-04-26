import streamlit as st
import requests
import json

# Streamlit app title
st.title("Edit Server Configurations")

# Form to edit servers.json
with st.form("edit_config_form"):
    st.subheader("Update Server Configuration")

    key = st.text_input("Key", placeholder="Enter the key")
    change_key = st.text_input("Change Key", placeholder="Enter the setting to change")
    value = st.text_input("Value", placeholder="Enter the new value")

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
