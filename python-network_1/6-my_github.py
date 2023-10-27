"""
Uses the GitHub API to display the user ID using Basic Authentication.
"""

import requests
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: {} <username> <personal_access_token>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    personal_access_token = sys.argv[2]
    
    # Construct the API URL for the authenticated user's information
    url = "https://api.github.com/user"
    
    # Create a Basic Authentication header using the provided personal access token
    headers = {
        "Authorization": "Basic {}:{}".format(username, personal_access_token)
    }
    
    # Send a GET request to the API URL with the Basic Authentication header
    response = requests.get(url, headers=headers)
    
    try:
        json_response = response.json()
        user_id = json_response.get("id")
        print(user_id)
    except ValueError:
        print("None")

if __name__ == "__main__":
    main()