#!/usr/bin/python3
import requests
import sys

def get_request_id(url):
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    return request_id

if __name__ == "__main__":
    url = sys.argv[1]
    request_id = get_request_id(url)
    print(request_id)
