import json, requests
from pikamon import *
from stats import *
import time
from cliente import *

# Creación de los pikamons
pikamon1 = Pikamon("Marciu", 100, "Grass")
pikamon2 = Pikamon("Jhonieru", 100, "Fire")
pikamon3 = Pikamon("Juan", 100, "Dudas")
pikamon4 = Pikamon("añañañin", 100, "ñatus")
pikamon5 = Pikamon("Goku", 7, "Jesuscrist")
pikamon6 = Pikamon("oni-chan", 69, "hentai")

# Stats de pikamons

# Bulbasur
pikamon1.currentHp = 45
pikamon1.defense = 49
pikamon1.speed = 45
pikamon1.spadefense = 65
pikamon1.spattack = 65
# Chimchar
pikamon2.currentHp = 44
pikamon2.defense = 44
pikamon2.speed = 58
pikamon2.spadefense = 44
pikamon2.spattack = 58
"""#Bulbasur
pikamon1.currentHp = 44
pikamon1.defense = 65
pikamon1.speed = 43
pikamon1.spadefense = 64
pikamon1.spattack = 50
#Bulbasur
pikamon1.currentHp = 45
pikamon1.defense = 49
pikamon1.speed = 45
#Bulbasur
pikamon1.currentHp = 45
pikamon1.defense = 49
pikamon1.speed = 45
#Bulbasur
pikamon1.currentHp = 45
pikamon1.defense = 49
pikamon1.speed = 45"""

pikamon1.attacks = [Attack("Tackle", "Physical", 35, 100), Attack("Vine wip", "Grass", 45, 100),
                    Attack("Sweet Scent", "Effect", 0, 100)]
pikamon2.attacks = [Attack("Scratch", "Physical", 40, 100), Attack("Fire Spin", "Fire", 50, 90),
                    Attack("Flame Wheel", "Fire", 60, 85)]
pikamon3.attacks = [Attack("Tackle", "Physical", 40, 100), Attack("Water Gun", "Water", 40, 100),
                    Attack("Hydro Pump", "Water", 110, 80)]
pikamon4.attacks = [Attack("scratch", "plant", 100, 93)]
pikamon5.attacks = [Attack("scratch", "plant", 100, 93)]
pikamon6.attacks = [Attack("scratch", "plant", 100, 93)]

# A pelear!


ip = input("Ingrese la ip del servidor: ")
player_name = input("ingrese su nick: ")
player_pikamon = input("ingrese el nombre del pikamon a usar: ")
getplayers(ip)

battle = Battle(pikamon1, pikamon2)

def tuTurno(pikamon):
    comando = None
    while not comando:
        # DO ATTACK -> attack 0
        tpm_comando = input("Qué deberia hacer " + pikamon.name + "?").split(" ")
        if (len(tpm_comando) == 2):
            try:
                if tpm_comando[0] == DO_ATTACK and 0 <= int(tpm_comando[1]) < 4:
                    comando = Comando({DO_ATTACK: int(tpm_comando[1])})
            except Exception:
                pass
    return comando


while not battle.isOver():
    comando1 = tuTurno(pikamon1)
    comando2 = tuTurno(pikamon2)

    turn = Turn()
    turn.comando1 = comando1
    turn.comando2 = comando2
    if turn.canStart():
        battle.executeTurn(turn)
