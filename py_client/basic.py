import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

#api_response = requests.get(endpoint, params={"abc": 123}, json={"query":"Hello World"} ) #HTTP request

api_response = requests.post(endpoint, json={"title":"title 1","content":"Hello World"} ) #HTTP request

print(api_response.json())