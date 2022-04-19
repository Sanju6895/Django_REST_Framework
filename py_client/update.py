import requests

endpoint = "http://localhost:8000/api/products/1/update/"

#api_response = requests.get(endpoint, params={"abc": 123}, json={"query":"Hello World"} ) #HTTP request

data = {
    "title": "Sanjay is awesome",
    "price": 999.99
}

api_response = requests.put(endpoint, json=data)#, 
            #json={"title":"title 1","content":"Hello World"} ) #HTTP request

print(api_response.json())