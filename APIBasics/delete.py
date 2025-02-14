import requests

#API URL
url = "https://reqres.in/api/users/2"

#Send GET Request
response = requests.delete(url)

#Printing
print(response.content)
print(response.headers)
print(response.status_code)
print(response.elapsed)

#Assertions
assert response.status_code == 204