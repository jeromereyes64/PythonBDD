import configparser

def getconfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\Jerome\\PycharmProjects\\PythonAPITesting\\utilities\\properties.ini')
    # check logs of config
    print(config.sections())
    print(config['API']['endpoint'])
    return config

def headercontent():
    header={'Content-Type':'application/json'}
    return header

def getuser():
    user = 'testUser'
    return user

def getpassword():
    password = 'testPassword'
    return password

def uploadpetimage(petid):
    return f'/api/v3/pet/{petid}/uploadImage'