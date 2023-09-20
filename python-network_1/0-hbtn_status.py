#!/usr/bin/python3
import requests

def fetch_status():
    """
    Fetches the status from https://alu-intranet.hbtn.io/status using requests module.
    Displays the response in a specific format.
    """
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content_type = type(response.text).__name__
    content = response.text
    
    print("Body response:")
    print("    - type: {}".format(content_type))
    print("    - content: {}".format(content))

if __name__ == "__main__":
    fetch_status()


