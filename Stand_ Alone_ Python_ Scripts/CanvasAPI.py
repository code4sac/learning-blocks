import json
import requests

# Define the URL separately
url = "http://canvas.instructure.com/api/v1/courses/[insert couse ID]/users"

# Set the access token in the headers
headers = {'Authorization': 'Bearer [insert api token]'}

try:
    # Use the 'requests' library to make a GET request
    r = requests.get(url, headers=headers)
    r.raise_for_status()  # Raise an exception if the response status code is not 200 (OK)

    # Check the response
    if r.status_code == 200:
        response_data = r.json()
        print(response_data)
    else:
        print(f"Error: {r.status_code}, {r.text}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
