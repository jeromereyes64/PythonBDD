import requests
from utilities.configurations import *

session_request = requests.session()
session_request.auth = auth=(getuser(),getpassword())
url = 'https://petstore3.swagger.io/api/v3/user/login'

response = session_request.get(url)

#assert status code
print(response.status_code)
assert response.status_code == 200