#/bin/env PYTHON3

from configparser import ConfigParser
from json import dumps
from requests import Session

from exceptions import RequestError
from inventory import Inventory

def main():
    conf = read_config('config.ini')

    # Set up session, authenticate, and store authentication token for the session duration
    session = Session()
    session.headers.update({'Content-Type': 'application/json', 'X-Okapi-Tenant': 'fs00001001'})
    token = authenticate(session, conf['baseurl'], conf['tenant'], conf['username'], conf['password'])
    session.headers.update({'X-Okapi-Tenant': conf['tenant']})
    session.headers.update({'X-Okapi-Token': token})
    
    # Get users
    # user_list = get_users(session, conf['baseurl'], max_users = 5)
    # print("User List:")
    # print(user_list)
    # Get items
    inventory = Inventory(session)
    item_list = inventory.get_items(session, conf['baseurl'], max_items = 5)
    print("Item List:")
    print(item_list)
    # Make list of loans
    # loan_list = generate_loans(user_list, item_list)
    #print(loan_list)
    # make_loans(session, conf['baseurl'], loan_list)
    # push loans to the 
    
def read_config(filename):
    config = ConfigParser()
    config.read(filename)
    return config['DEFAULT']

def authenticate(session, baseurl, tenant, username, password):
    """Authenticate to Okapi and get an authentication token
    """
    r = session.post(baseurl+'/authn/login',
                     data = dumps({'username': username, 'password': password}))
    #print(r.status_code)
    # TODO: Maybe get rid of AuthenticationError class 
    r.raise_for_status()
    if r.status_code != 201:
        raise RequestError(r.status_code, r.text, r.url, req_headers= r.request.headers)
    return r.headers.get('x-okapi-token')

if __name__ == "__main__":
    # execute only if run as a script
    main()