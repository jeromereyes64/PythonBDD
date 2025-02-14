import requests
from utilities.configurations import *

url = getconfig()['API']['endpoint'] + uploadpetimage(10)
print(url)
files = {'file': open('C:\\Users\\Jerome\\PycharmProjects\\PythonAPITesting\\Files\\Passport.png', 'rb')}

response = requests.post(url,
            files = files,)

#put response in dictionary
dict_response = response.json()

#check response
print(response.status_code)
print(response.text)