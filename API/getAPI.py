import requests
from utilities.configurations import *
from utilities.resources import *
from utilities.payload import *
import json

url = getconfig()['API']['endpoint'] + apiResources.findPet
response = requests.get(url,
             params= {'status':'available'})

#put response in list
json_response = response.json()
print(json_response)
print(type(json_response))

print(json_response[0]['category'])

#assert response status code
assert response.status_code == 200

#assert response header
print(response.headers)
assert response.headers['Content-Type'] == 'application/json'

#loop in result and assert
for pets in json_response:
    if pets['name'] == 'Cat 2':
        print(pets)
        assert pets == expectedResultAssert()
        break