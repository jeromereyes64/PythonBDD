import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"

#Send Get Request
response = requests.get(url)

#Parse Response to JSON Text
json_response = json.loads(response.text)
# print(json_response)

#fetch value using jsonpath
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])

#assertion
assert pages[0] == 2


#fetch firstname
#fetch value using JsonPath

for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, f'data[{i}].first_name')
    print(first_name[0])