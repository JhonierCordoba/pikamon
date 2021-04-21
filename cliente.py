import requests
import json


class cliente:

    def __init__(self, ip, nick, pokemon):
        self.ip = ip
        self.nick = nick
        self.pokemon = pokemon

    def get_ip(self):
        return self.ip

    def get_nick(self):
        return self.nick

    def get_pokemon(self):
        return self.pokemon

    def set_ip(self, new_ip):
        self.ip = new_ip

    def set_nick(self, new_nick):
        self.nick = new_nick

    def set_pokemon(self, new_pokemon):
        self.pokemon = new_pokemon


def getplayers(ip):
    url = "http://" + ip + ":5000/players"

    headers = {"Content-Type": "application/json"}

    response = requests.request("GET", url, headers=headers)
    answerjson = response.json()
    print(response.text)
