import json

courses = '{"name": "Jerome", "languages": [ "Test1", "Test2"]}'

#Parse JSON String to dictionary
dic_test = json.loads(courses)
print(type(dic_test))
print(dic_test['name'])

#put the language to a list array
list_test = dic_test['languages']
print(type(list_test))
print(list_test[0])