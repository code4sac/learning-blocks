import requests
import json

# Define the URL separately
url = "http://canvas.instructure.com/api/v1/courses/7983596/users"

# Set the access token in the headers
headers = {'Authorization': 'Bearer 7~skPyx76YuDnhaacL9yYF4Kt5n9UrWptdSNWg4WNk01PIQt18RGna3lzFlOmruUum'}

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
