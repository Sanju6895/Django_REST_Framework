import requests

endpoint = "http://localhost:8000/api/products/1/"

#api_response = requests.get(endpoint, params={"abc": 123}, json={"query":"Hello World"} ) #HTTP request

api_response = requests.get(endpoint)#, 
            #json={"title":"title 1","content":"Hello World"} ) #HTTP request

print(api_response.json())