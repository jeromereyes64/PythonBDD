import requests

header_data = {
    'T1' : 'Fist',
    'T2' : 'Second'
}

response = requests.get('https://httpbin.org/get', headers= header_data)
print(response.text)