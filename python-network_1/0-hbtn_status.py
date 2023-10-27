"""
Fetches a URL using the requests package and displays the body response.
"""
import requests

def fetch_hbtn_status():
    url = 'https://alu-intranet.hbtn.io/status'
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Display the body response details
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

if __name__ == "__main__":
    fetch_hbtn_status()

