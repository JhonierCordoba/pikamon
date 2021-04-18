from stats import *

class Pikamon():

    def __init__ (self, name, level, element):
        self.name = name
        self.level = level
        self.type = element
        self.attacks = []
        self.stats = {}
        self.currentStatus = 0
        self.currentHp = 0

    """def stats(stat):
        val1 = (2*self.stats[stat])
        pass
    def standarStat(self):
        pass
    def hpStat(self):
        val1 = (2*self.stats[stat]+self.stats()"""

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
        if DO_ATTACK in comando1.action.keys():
            attack1 = self.pikamon1.attacks[comando1.action[DO_ATTACK]]
        if DO_ATTACK in comando2.action.keys():
            attack2 = self.pikamon2.attacks[comando2.action[DO_ATTACK]]
        self.pikamon2.currentHp -= attack1.damage
        self.pikamon1.currentHp -= attack2.damage
        self.actualTurn += 1

    def isOver(self):
        finished = self.pikamon1.currentHp <= 0 or self.pikamon2.currentHp <= 0
        if finished:
            self.Winner()
        return finished

    def status(self):
        """if(self.pikamon1.currentHp <= 0 or self.pikamon2.currentHp <= 0):
            return """
        print(self.pikamon1.name, " tiene ", str(self.pikamon1.currentHp), "ps restantes!")
        print(self.pikamon2.name, " tiene ", str(self.pikamon2.currentHp), "ps restantes!")

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

class Comando():

    def __init__ (self, action):
        self.action = action

class Turn():

    def __init__ (self):
        self.comando1 = None
        self.comando2 = None

    def canStart(self):
        return self.comando1 is not None or self.command2 is not None




