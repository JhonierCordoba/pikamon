from stats import *
import random

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

class Attack():
     def __init__(self, name, element, damage, accuracy):
        self.name = name
        self.type = element
        self.damage = damage
        self.accuracy = accuracy

class Battle():

    def __init__(self, pikamon1, pikamon2):
        self.pikamon1 = pikamon1
        self.pikamon2 = pikamon2
        self.actualTurn = 0

    def executeTurn(self, turn):
        comando1 = turn.comando1
        comando2 = turn.comando2
        attack1 = None
        attack2 = None
        if self.pikamon1.speed > self.pikamon2.speed:
            if DO_ATTACK in comando1.action.keys():
                attack1 = self.pikamon1.attacks[comando1.action[DO_ATTACK]]
                print(self.pikamon1.name, " used ", attack1.name, " !")
            #self.pikamon2.currentHp -= attack1.damage
            self.pikamon2.currentHp -= self.computeDamage(attack1, self.pikamon1, self.pikamon2)
            self.pikamon2.currentHp = round(self.pikamon2.currentHp)
            self.status(self.pikamon2)
            if DO_ATTACK in comando2.action.keys() and  self.pikamon2.currentHp > 0:
                attack2 = self.pikamon2.attacks[comando2.action[DO_ATTACK]]
                print(self.pikamon2.name, " used ", attack2.name, " !")
            #self.pikamon1.currentHp -= attack2.damage
            self.pikamon1.currentHp -= self.computeDamage(attack2, self.pikamon2, self.pikamon1)
            self.pikamon1.currentHp = round(self.pikamon1.currentHp)
            self.status(self.pikamon1)
        else:
            if DO_ATTACK in comando2.action.keys():
                attack2 = self.pikamon2.attacks[comando2.action[DO_ATTACK]]
                print(self.pikamon2.name, " used ", attack2.name, " !")
            #self.pikamon1.currentHp -= attack2.damage
            self.pikamon1.currentHp -= self.computeDamage(attack2, self.pikamon2, self.pikamon1)
            self.pikamon1.currentHp = round(self.pikamon1.currentHp)
            self.status(self.pikamon1)
            if DO_ATTACK in comando1.action.keys() and self.pikamon1.currentHp > 0:
                attack1 = self.pikamon1.attacks[comando1.action[DO_ATTACK]]
                print(self.pikamon1.name, " used ", attack1.name, " !")
            #self.pikamon2.currentHp -= attack1.damage
            self.pikamon2.currentHp -= self.computeDamage(attack1, self.pikamon1, self.pikamon2)
            self.pikamon2.currentHp = round(self.pikamon2.currentHp)
            self.status(self.pikamon2)
        self.actualTurn += 1

    def computeDamage(self, attack, pikamon1, pikamon2):
        if attack.type == "Physical":
            powerFactor = (attack.damage / pikamon2.defense)
        else:
            powerFactor = (pikamon1.spattack / pikamon2.spadefense)
        damage_without_modifier = float(powerFactor) / 50 + 2
        finalDamage = damage_without_modifier * self.computeDamageModifier(attack, pikamon1, pikamon2)
        print("FINAL DAMAGE", finalDamage, pikamon1.name, "to", pikamon2.name)
        return finalDamage

    def computeDamageModifier(self, attack, pikamon1, pikamon2):
        # Compute STAB
        effectiveness = 0
        stab = 1.5
        if pikamon1.type == pikamon2.type:
            effectiveness = 1/2
        elif pikamon1.type == "Fire" and pikamon2.type == "Water":
            effectiveness = 1 / 2
        elif pikamon1.type == "Water" and pikamon2.type == "Grass":
            effectiveness = 1 / 2
        elif pikamon1.type == "Fire" and pikamon2.type == "Grass":
            effectiveness = 2
        elif pikamon1.type == "Water" and pikamon2.type == "Fire":
            effectiveness = 2
        elif pikamon1.type == "Grass" and pikamon2.type == "Water":
            effectiveness = 2
        elif pikamon1.type == "Grass" and pikamon2.type == "Fire":
            effectiveness = 1/2

        # Calcular Critico
        critical = 1
        if random.random() <= 0.1:
            print(pikamon1.name, "did a critical attack!!")
            critical = 1.5
        return stab * effectiveness * critical

    def isOver(self):
        finished = self.pikamon1.currentHp <= 0 or self.pikamon2.currentHp <= 0
        if finished:
            self.Winner()
        return finished

    def status(self, pikamon):
        print(pikamon.name, " tiene ", str(pikamon.currentHp), "ps restantes!")


    def Winner(self):
        if self.pikamon1.currentHp <= 0 < self.pikamon2.currentHp:
            print(self.pikamon2.name, " won in ", str(self.actualTurn), "turns!")
        elif self.pikamon2.currentHp <= 0 < self.pikamon1.currentHp:
            print(self.pikamon1.name, " won in ", str(self.actualTurn), "turns!")
        else:
            print("Double KO!!!")

    def ejecutarTurno(self, turn):
        comando1 = turn.comando1
        comando2 = turn.comando2
        attack1 = None
        attack2 = None
        if DO_ATTACK in comando1.action.keys():
            attack1 = self.pikamon1.attacks[comando1.action[DO_ATTACK]]
        if DO_ATTACK in comando2.action.keys():
            attack2 = self.pikamon2.attacks[comando1.action[DO_ATTACK]]

class Comando():

    def __init__ (self, action):
        self.action = action

class Turn():

    def __init__ (self):
        self.comando1 = None
        self.comando2 = None

    def canStart(self):
        return self.comando1 is not None or self.command2 is not None




