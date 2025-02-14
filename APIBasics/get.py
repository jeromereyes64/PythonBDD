import requests

#API URL
url = "https://reqres.in/api/users?page=2"


def test_get_user():
    #Send GET Request
    response = requests.get(url)

    #Printing
    print(response.content)
    print(response.headers)
    print(response.status_code)
    print(response.elapsed)

    #Assertion
    assert response.status_code == 200
    assert response.elapsed.total_seconds() * 1000 <= 2000, f"Response time exceeded: {response.elapsed.total_seconds() * 1000}ms"
