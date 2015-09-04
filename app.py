import os
import json
import requests
import requests.auth
import time
import re
import random
import urllib3

def getConfig():
    curPath = os.getcwd()
    data = []
    with open('%s/config.json' % curPath, 'rb') as f:
        data = json.load(f)
    f.close()
    return data

def token():
    config = getConfig()
    client_auth = requests.auth.HTTPBasicAuth(config['client_ID'], config['client_secret'])
    post_data = {
        "grant_type": "password",
        "username": config['user'],
        "password": config['password']
    }
    headers = {"User-Agent": "PINTClient/0.1 by PINT_HR"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    res = response.json()
    #print json.dumps(res)
    return res['access_token']

def getMe(headers):
    '''
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED', # Force certificate check.
        ca_certs='/Library/Python/2.7/site-packages/certifi/cacert.pem'
    )
    try:
        response = http.request(
            'GET', "https://oauth.reddit.com/api/v1/me", headers=headers
    )
    except urllib3.exceptions.SSLError as e:
        print 'SSL Cert not valid'
    return response.read(decode_content=True)
    '''

    response = requests.get(
        "https://oauth.reddit.com/api/v1/me", headers=headers
    )
    return response.json()

def getMsgs(headers):
    params = {
        'limit': 100,
        'count': 0
    }
    response = requests.get(
        "https://oauth.reddit.com/message/unread",
        headers=headers,
        params=params
    )
    return response.json()


def getNotifications(token):
    response = requests.get(
        "https://oauth.reddit.com/api/v1/me", headers=headers
    )
    return response.json()

if __name__ == "__main__":
    urllib3.disable_warnings()
    token = token()
    headers = {
        "Authorization": "bearer " + token,
        "User-Agent": "PINTClient/0.1 by PINT_HR"
    }
    meDict = getMe(headers)
    print json.dumps(meDict)
    notesDict = getMsgs(headers)
    print json.dumps(notesDict)
