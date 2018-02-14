import requests

# Global variables
_Headers = {}


def logIn():
    user = 'jofriasg@pa.uc3m.es'
    passwd = 'compass'

    response = requests.post(_url('login/'), json={
        "email": user,
        "password": passwd
    })
    key = response.content                              # I think this is the key

    addToParameters('rest-compass-token', key)

def addToParameters(key, value):
    _Headers[key] = value

def _url(path):
    # return 'http://195.130.109.197:8080/jspui/' + path            # This server is down
    # return 'http://learning-compass.teiath.gr:8080/jspui/' + path
    return 'http://learning-compass.teiath.gr:8080/rest/' + path
    # return 'http://195.130.109.197:8080/rest/' + path            # This server is down


def get_test():
    return requests.get(_url('test'), headers = _Headers)


# Test code
logIn()
a = get_test()
print(a)