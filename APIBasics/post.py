import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users"

#read input json file
file_open = open('post.json','r')
json_read = file_open.read()
json_data = json.loads(json_read)

#make post request with json
response = requests.post(url,json_data)

#assert
assert response.status_code == 201

#parse json response
json_data = json.loads(response.text)
print(json_data)

#assert the id
data = jsonpath.jsonpath(json_data,'name')
assert data[0] == 'test', f"Response name data is incorrect"

#print
print(response.status_code)
print(response.headers)
print(response.headers.get('Date'))



