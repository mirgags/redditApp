import os
import json
import requests
import requests.auth
import time
import re
import random

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
    print json.dumps(res)
    return res['access_token']

def getMe(headers):
    response = requests.get(
        "https://oauth.reddit.com/api/v1/me", headers=headers
    )
    return response.json()

def getNotifications(token):
    response = requests.get(
        "https://oauth.reddit.com/api/v1/me", headers=headers
    )
    return response.json()

if __name__ == "__main__":
    token = token()
    headers = {
        "Authorization": "bearer " + token,
        "User-Agent": "PINTClient/0.1 by PINT_HR"
    }
    meDict = getMe(headers)
    print json.dumps(meDict)
    notesDict = getNotifications(headers)
    print json.dumps(notesDict)
