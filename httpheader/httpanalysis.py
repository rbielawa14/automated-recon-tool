import requests

def get_http_headers(domain):
    response = requests.get(domain)
    print(response.headers)
