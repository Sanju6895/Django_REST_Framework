import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/api/products/auth/"
username = input("Whats your username \n")
password = getpass("Enter Password\n")
auth_response = requests.post(auth_endpoint, json={"username":username,"password":password}) 
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    api_response = requests.get(endpoint, headers=headers) 
    print(api_response.json())