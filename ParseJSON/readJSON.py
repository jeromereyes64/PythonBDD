import json

#parse JSON
with open('C:\\Users\\Jerome\\PycharmProjects\\PythonAPITesting\\ParseJSON\\course.json') as reader:
    #store in dictionary
    dict_test = json.load(reader)
    print(type(dict_test))
    print(dict_test)
    print(dict_test['courses'][2]['title'])
    print(dict_test['dashboard']['stats']['ongoingCourses'])
    print(dict_test['dashboard']['title'])

    #loop in courses
    print(type(dict_test['courses']))
    for courses in dict_test['courses']:
        if courses['title'] == 'Advanced JavaScript':
            print('this is the correct record')
            print(courses)
            assert courses['status'] == 'ongoing'