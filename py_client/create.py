import requests

endpoint = "http://localhost:8000/api/products/"

#api_response = requests.get(endpoint, params={"abc": 123}, json={"query":"Hello World"} ) #HTTP request

api_response = requests.post(endpoint,
        json={"title":"Spanish Giants","content":"You know its Real Madrid CF"} ) #HTTP request

print(api_response.json())