import requests

param_data = {
    'name' : 'test',
    'address' : 'test'
}

response = requests.get('https://httpbin.org/get', params= param_data)
print(response.text)