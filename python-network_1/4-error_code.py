#!/usr/bin/python3
import requests
import sys

def fetch_url_content(url):
    response = requests.get(url)
    
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url_content(url)
