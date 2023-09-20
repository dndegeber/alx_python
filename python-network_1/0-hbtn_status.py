import requests

def fetch_status():
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content_type = type(response.text).__name__
    content = response.text
    
    print("Body response:")
    print(f"    - type: {content_type}")
    print(f"    - content: {content}")

if __name__ == "__main__":
    fetch_status()
