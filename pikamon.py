from stats import *
import random
#Clase pikamon
class Pikamon():

    def __init__ (self, name, level, element):
        self.name = name
        self.level = level
        self.type = element
        self.attacks = []
        self.defense = 0
        self.spattack = 0
        self.spadefense = 0
        self.speed = 0
        self.stats = {}
        self.currentStatus = 0
        self.currentHp = 0
#Clase ataque
class Attack():
     def __init__(self, name, element, damage, accuracy):
        self.name = name
        self.type = element
        self.damage = damage
        self.accuracy = accuracy
#Clase batalla, para la simulación de los turnos
class Battle():

    def __init__(self, pikamon1, pikamon2):
        self.pikamon1 = pikamon1
        self.pikamon2 = pikamon2
        self.actualTurn = 0

    # Función que ejecuta un turno
    def executeTurn(self, turn, pikamon1, pikamon2):
        # recibe comandos
        comando1 = turn.comando1
        self.pikamon1 = pikamon1
        self.pikamon2 = pikamon2
        attack1 = None
        self.attack(comando1)

    def attack(self, comando1):
        if DO_ATTACK in comando1.action.keys():
            # se lo asigna a la variable
            attack1 = self.pikamon1.attacks[comando1.action[DO_ATTACK]]
        print(self.pikamon1.name, " usó ", attack1.name, " !")
            # le resta la vida a el pikamon que recibió el ataque
        self.pikamon2.currentHp -= self.computeDamage(attack1, self.pikamon1, self.pikamon2)
        self.pikamon2.currentHp = round(self.pikamon2.currentHp)
        self.status(self.pikamon2)

    # Calcula el daño
    def computeDamage(self, attack, pikamon1, pikamon2):
        if attack.type == "Físico":
            powerFactor = ((attack.damage*8) / pikamon2.defense)
            damage_without_modifier = float(powerFactor) / 7 + 1
            finalDamage = damage_without_modifier * 2 + damage_without_modifier
        else:
            powerFactor = ((pikamon1.spattack*5+attack.damage*3) / pikamon2.spadefense)
            damage_without_modifier = float(powerFactor) / 7 + 1
            finalDamage = damage_without_modifier * self.computeDamageModifier(attack, pikamon1, pikamon2) + damage_without_modifier
        """if random.random() >= attack.accuracy/100:
            finalDamage = 0
            print(pikamon1.name, " falló su ataque")"""
        #else:
        print(pikamon1.name, " Hizo ", round(finalDamage), " de daño a ", pikamon2.name)
        return finalDamage

    # Calcula los criticos y las ventajas elementales
    def computeDamageModifier(self, attack, pikamon1, pikamon2):
        # Compute STAB
        effectiveness = 0
        stab = 1.5
        if pikamon1.type == pikamon2.type:
            effectiveness = 1/2
        elif pikamon1.type == "Fuego" and pikamon2.type == "Agua":
            effectiveness = 1 / 2
        elif pikamon1.type == "Agua" and pikamon2.type == "Hierba":
            effectiveness = 1 / 2
        elif pikamon1.type == "Fuego" and pikamon2.type == "Hierba":
            effectiveness = 2
        elif pikamon1.type == "Agua" and pikamon2.type == "Fuego":
            effectiveness = 2
        elif pikamon1.type == "Hierba" and pikamon2.type == "Agua":
            effectiveness = 2
        elif pikamon1.type == "Hierba" and pikamon2.type == "Fuego":
            effectiveness = 1/2

        # Calcular Critico
        critical = 1
        """if random.random() <= 0.1:
            print(pikamon1.name, "hizo un ataque crítico!!")
            critical = 2.5"""
        return stab * effectiveness * critical

    # Se ejecuta cuando se acaba la batalla(Sí uno de los 2 muere)
    def isOver(self):
        finished = self.pikamon1.currentHp <= 0 or self.pikamon2.currentHp <= 0
        if finished:
            self.Winner()
        return finished

    # Muestra la salud restante del pikamon
    def status(self, pokemon):
        print(pokemon.name, " tiene ", str(pokemon.currentHp), "ps restantes!")

    # Define un ganador
    def Winner(self):
        if self.pikamon1.currentHp <= 0 < self.pikamon2.currentHp:
            print(self.pikamon2.name, " won in ", str(self.actualTurn), "turns!")
        elif self.pikamon2.currentHp <= 0 < self.pikamon1.currentHp:
            print(self.pikamon1.name, " won in ", str(self.actualTurn), "turns!")
        else:
            print("Double KO!!!")

# Clase comando para lo que se ingresa por consola
class Comando():

    def __init__ (self, action):
        self.action = action
# Clase turno, para turnos obvi
class Turn():

    def __init__ (self):
        self.comando1 = None
        self.comando2 = None

    def canStart(self):
        return self.comando1 is not None or self.command2 is not None




