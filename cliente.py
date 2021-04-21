"""import requests"""
import json


def getplayers(ip):
    url = "http://" + ip + ":5000/players"

    headers = {"Content-Type": "application/json"}

    response = requests.request("GET", url, headers=headers)
    answerjson = response.json()
    print(response.text)
