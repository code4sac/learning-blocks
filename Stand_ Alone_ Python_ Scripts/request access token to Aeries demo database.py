import base64
import requests


def get_access_token(client_id, client_secret):
    # Base64 encode the client ID and client secret
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    # Define headers
    headers = {
        "Authorization": f"Basic {credentials}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    # Define token endpoint and payload
    token_endpoint = "https://demo.aeries.net/aeries"  # Update with correct endpoint
    token_payload = {"grant_type": "client_credentials"}

    try:
        # Make the POST request to acquire the access token
        response = requests.post(token_endpoint, headers=headers, data=token_payload)

        # Print response status and text for debugging
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        # Check the response status code
        if response.status_code == 200:
            try:
                # Parse the JSON response
                token_info = response.json()
                access_token = token_info.get("access_token")
                # Return the access token
                return access_token
            except ValueError as e:
                print(f"Error parsing JSON: {e}")
                return None
        else:
            # Print the error message
            print(f"Failed to obtain access token: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


# Example usage
client_id = "1279e5c6b747b6d62b7c76db3a205d40eb7458e678a90493d537d5af6b953550"
client_secret = "68019dbf8d8ba82980dd148eecc3977ac0d7f1f040d444225874c88eb80b9c1a"
token = get_access_token(client_id, client_secret)
print(f"Access Token: {token}")
