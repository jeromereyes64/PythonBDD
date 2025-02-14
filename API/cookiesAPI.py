import requests

#Use cookies
cookie = {'visit-month':'February'}
response = requests.get('http://rahulshettyacademy.com', cookies = cookie)
print(response.status_code)


#store cookies in session manager
session_request = requests.session()
session_request.cookies.update({'visit-month':'February'})

response = session_request.get('http://rahulshettyacademy.com')
print(response.text)