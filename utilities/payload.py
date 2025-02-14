def addpet(petID):
    body={
   "id":petID,
   "name":"doggie",
   "category":{
      "id":1,
      "name":"Dogs"
   },
   "photoUrls":[
      "string"
   ],
   "tags":[
      {
         "id":0,
         "name":"string"
      }
   ],
   "status":"available"
   }
    return body

def expectedResultAssert():
    expectedResult = {
        "id": 2,
        "category": {
            "id": 2,
            "name": "Cats"
        },
        "name": "Cat 2",
        "photoUrls": [
            "url1",
            "url2"
        ],
        "tags": [
            {
                "id": 1,
                "name": "tag2"
            },
            {
                "id": 2,
                "name": "tag3"
            }
        ],
        "status": "available"
    }
    return expectedResult