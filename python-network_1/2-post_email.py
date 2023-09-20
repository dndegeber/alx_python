#!/usr/bin/python3
import requests
import sys

def post_email(url, email):
    payload = {'email': email}
    response = requests.post(url, data=payload)
    return response.text

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = post_email(url, email)
    print(response_body)
