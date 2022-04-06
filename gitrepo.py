# utility for retrieving repo info
import os
import requests


def repo(username):
    api_key=os.environ.get("api_key")
    url=f"https://api.github.com/users/{username}"
    head={
        "Accept": "application/vnd.github.v3+json",
        'Authorization':'token ' + api_key
    }
    r=requests.get(url,headers=head)
    jsonResponse = r.json()
    print(r.json())
    for key, value in jsonResponse.items():
        print(key, ":", value)
    try:
        return r.json()
    except Exception:
        return f"Please check your username or api key"

uname = input("Enter your github username:  ")
repo(uname)