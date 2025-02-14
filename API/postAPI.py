import requests
from utilities.resources import *
from utilities.configurations import *
from utilities.payload import *

url = getconfig()['API']['endpoint'] + apiResources.addPet
response = requests.post(url,
            json=addpet(10),
            headers=headercontent(),)

#put response in dictionary
dict_response = response.json()
print(dict_response)
print(type(dict_response))

#get ID of PET
petID = dict_response['id']
print(petID)

#assert status code
assert response.status_code == 200


#DELETE REQUEST
del_response = requests.delete(f'{url}/{petID}')

# Check if the response is empty
if not del_response.text.strip():  # If the response text is empty or whitespace
    print(f"Response is empty. Status code: {del_response.status_code}")
else:
    # Try to parse JSON if the response is not empty
    try:
        dict_response_del = del_response.json()
        print("Delete response JSON:", dict_response_del)
    except ValueError:
        print("Response is not valid JSON:", del_response.text)

#assert status code
assert del_response.status_code == 200

#assert response text
assert del_response.text == 'Pet deleted'