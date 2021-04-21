import requests
import json


class cliente:
    def __init__(self, name, pokemon, ip):
        self.nick = name
        self.pokemon = pokemon
        self.ip = ip

    def get_name(self):
        return self.nick

    def get_pokemon(self):
        return self.pokemon

    def cargar_cliente(self):
        import requests

        url = "http://" + self.ip + ":5000/players"

        payload = {
            "name": self.nick,
            "pokemon": self.pokemon
        }
        headers = {"Content-Type": "application/json"}

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

    def getplayers(self):
        url = "http://" + self.ip + ":5000/players"

        headers = {"Content-Type": "application/json"}

        response = requests.request("GET", url, headers=headers)
        answerjson = response.json()
        print(response.text)

    def get_enemy_pokemon(self):
        url = "http://" + self.ip + ":5000/players/matches/"+self.nick

        headers = {"Content-Type": "application/json"}

        response = requests.request("GET", url, headers=headers)
        answerjson = response.json()
        name = answerjson["pelea"][0]["name"]
        print(name)
        pokemon = answerjson["pelea"][0]["pokemon"]
        print(pokemon)
        enemy = cliente(name, pokemon, self.ip)
        return enemy

    def wait(self):
        url = "http://" + self.ip + ":5000/wait/"+self.nick

        headers = {"Content-Type": "application/json"}

        response = requests.request("GET", url, headers=headers)
        answerjson = response.json()
        wait = answerjson["espera"][0]["wait"]
        if wait == "true":
            return True
        else:
            return False
