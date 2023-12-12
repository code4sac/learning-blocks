import requests
from base64 import b64encode

# Replace these values with your actual client ID and client secret
client_id = "your_client_id"
client_secret = "your_client_secret"

# Base64 encode the client ID and client secret
credentials = b64encode(f"{client_id}:{client_secret}".encode()).decode()

# Define headers
headers = {
    "Authorization": f"Basic {credentials}",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
}

# Define token endpoint and payload
token_endpoint = "https://demo.aeries.net/aeries/token"
token_payload = {"grant_type": "client_credentials"}

# Make the POST request to acquire the access token
response = requests.post(token_endpoint, headers=headers, data=token_payload)

# Handle the response, parse JSON, and extract the access token
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data.get("access_token")
    print(f"Access Token: {access_token}")
else:
    print(f"Token request failed with status code {response.status_code}")
    print(response.text)
