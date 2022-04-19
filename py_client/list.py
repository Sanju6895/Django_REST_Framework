import requests

endpoint = "http://localhost:8000/api/products/"

#api_response = requests.get(endpoint, params={"abc": 123}, json={"query":"Hello World"} ) #HTTP request

api_response = requests.get(endpoint) 

print(api_response.json())