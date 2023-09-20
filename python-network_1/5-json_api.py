#!/usr/bin/python
import requests
import sys

def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}

    response = requests.post(url, data=payload)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
