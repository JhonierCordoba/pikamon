"""import json, requests"""
import pygame
from pikamon import *
from stats import *
import time
from cliente import *

# Crea el juego como tal
"""class Game:
    def __init__(self, pikamon1, pikamon2):
        self.buttons = []
        #self.menu = Menu()
        #self.gui = GUI()
        self.bg = None
        pygame.init()
        # Crea la ventana del juego
        self.screen = pygame.display.set_mode((160 * 4, 144 * 4))

        #clock = pygame.time.Clock()
        #clock.tick(60)

    # Prosesos de la ventana
    def process(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.stopped = True
            for button in self.buttons:
                button.handle_event(event, self)
            self.menu.handle_event(event, self)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print(event.pos)

    # Más procesos, siga bajando
    def loadResources(self):
        self.loadPokemonImage(self.pikamon1, True)
        self.loadPokemonImage(self.pikamon2, False)
        self.gui.loadResources()

    # Más mierda jajajaja
    def loadPokemonImage(self, pikamon, isPlayer):
        pokemon_name = pikamon.name.lower()
        if isPlayer:
            pokemon_img = pygame.image.load(pokemon_name + "_Back.png")
            pokemon_img = pygame.transform.scale(pokemon_img, (300, 300))
            pikamon.renderer = pokemon_img
        else:
            pokemon_img = pygame.image.load('Bulbasaur_Front' + pokemon_name + ".png")
            pokemon_img = pygame.transform.scale(pokemon_img, (200, 200))

            pikamon.renderer = pokemon_img
        #self.bg = pygame.image.load('res/battle_bg/battle_bg_1.png')
        #self.bg = pygame.transform.scale(self.bg, (160 * 4, 400))
"""


# Creación de los pikamons
pikamon1 = Pikamon("Pikasaur", 100, "Hierba")
pikamon2 = Pikamon("Pikarizard", 100, "Fuego")
pikamon3 = Pikamon("Pikquirle", 100, "Agua")
pikamon4 = Pikamon("añañañin", 100, "ñatus")
pikamon5 = Pikamon("Goku", 7, "Jesuscrist")
pikamon6 = Pikamon("oni-chan", 69, "kai")

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
#Squirle
pikamon3.currentHp = 50
pikamon3.defense = 30
pikamon3.speed = 62
pikamon3.spadefense = 70
pikamon3.spattack = 50
"""#Bulbasur
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

pikamon1.attacks = [Attack("Tackle", "Físico", 35, 100), Attack("Vine wip", "Hierba", 45, 90),
                    Attack("Green cannon", "Hierba", 200, 60)]
pikamon2.attacks = [Attack("Scratch", "Físico", 40, 100), Attack("Fire Spin", "Fuego", 50, 90),
                    Attack("Flame Wheel", "Fuego", 120, 75)]
pikamon3.attacks = [Attack("Tackle", "Físico", 40, 100), Attack("Water Gun", "Agua", 40, 90),
                    Attack("Hydro Pump", "Agua", 110, 80)]
pikamon4.attacks = [Attack("scratch", "plant", 100, 93)]
pikamon5.attacks = [Attack("scratch", "plant", 100, 93)]
pikamon6.attacks = [Attack("scratch", "plant", 100, 93)]

# A pelear!


"""ip = input("Ingrese la ip del servidor:")
player_name = input("ingrese su nick: ")
player_pikamon = input("ingrese el nombre del pikamon a usar: ")

getplayers(ip)"""
"""game = Game(pikamon1, pikamon2)
game.loadPokemonImage(pikamon1, True)"""

print("Escoge un pikamon: ")
pikalist = [pikamon1, pikamon2, pikamon3]
print(f"1. {pikamon1.name}, {pikamon1.type}, {pikamon1.currentHp}")
print(f"2. {pikamon2.name}, {pikamon2.type}, {pikamon2.currentHp}")
print(f"3. {pikamon3.name}, {pikamon3.type}, {pikamon3.currentHp}")
pika1 = pikalist[int(input())-1]
print("Has seleccionado a ", pika1.name)

if pika1.speed > pikamon1.speed:
    battle = Battle(pika1, pikamon1)
else:
    battle = Battle(pikamon1, pika1)

#Aquí comienzan los turnos
def tuTurno(pikamon):
    comando = None
    while not comando:
        # DO ATTACK -> attack 0
        tpm_comando = input(f"Qué deberia hacer {pikamon.name}?| Attack 0 = {pikamon.attacks[0].name}, Attack 1 = {pikamon.attacks[1].name}, Attack 2 = {pikamon.attacks[2].name} \n").split(" ")
        if (len(tpm_comando) == 2):
            try:
                if tpm_comando[0] == DO_ATTACK and 0 <= int(tpm_comando[1]) < 3:
                    comando = Comando({DO_ATTACK: int(tpm_comando[1])})
            except Exception:
                pass
    return comando

#La batalla epica por la nota
N = 0
while not battle.isOver():
    if(N % 2 == 0):
        comando1 = tuTurno(pika1)
        turn = Turn()
        turn.comando1 = comando1
        if turn.canStart():
            battle.executeTurn(turn, pika1, pikamon1)
    else:
        comando1 = tuTurno(pikamon1)
        turn = Turn()
        turn.comando1 = comando1
        if turn.canStart():
            battle.executeTurn(turn, pikamon1, pika1)
    N += 1

