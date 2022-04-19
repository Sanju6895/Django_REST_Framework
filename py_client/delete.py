import requests

product_id = input("Enter product id to be used\n")


try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not valid")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    api_response = requests.delete(endpoint)
    print(api_response.status_code)  