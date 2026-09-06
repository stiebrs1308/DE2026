# importing Flask and other modules
import requests

# See https://www.w3schools.com/python/module_requests.asp
response = requests.get('http://127.0.0.1:5001/users?name=sukamanupimpi')
print(response.status_code)
print(response.text)
