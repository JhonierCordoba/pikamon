from pikamon import *
from stats import *
import time

# Creación de los pikamons
pikamon1 = Pikamon("Marciu", 100, "Melena")
pikamon2 = Pikamon("Jhonieru", 99, "Black")
pikamon3 = Pikamon("Juan", 66, "Dudas")
pikamon4 = Pikamon("añañañin", 88, "ñatus")
pikamon5 = Pikamon("Goku", 77, "Jesuscrist")
pikamon6 = Pikamon("oni-chan", 69, "hentai")

pikamon1.currentHp = 80
pikamon2.currentHp = 60

# Stats de pikamons
pikamon1.stats = {
    ATTACK: 80,
    SPATTACK: 25,
    HP: 100,
    DEFENSE: 49,
    Speed: 45,
}
pikamon2.stats = {
    ATTACK: 60,
    SPATTACK: 35,
    HP: 120,
    DEFENSE: 49,
    Speed: 45,
}
pikamon3.stats = {
    ATTACK: 49,
    SPATTACK: 65,
    HP: 45,
    DEFENSE: 49,
    Speed: 45,
}
pikamon4.stats = {
    ATTACK: 5,
    SPATTACK: 65,
    HP: 45,
    DEFENSE: 49,
    Speed: 45,
}
pikamon5.stats = {
    ATTACK: 2,
    SPATTACK: 65,
    HP: 45,
    DEFENSE: 49,
    Speed: 45,
}
pikamon6.stats = {
    ATTACK: 49,
    SPATTACK: 65,
    HP: 45,
    DEFENSE: 49,
    Speed: 45,
}

pikamon1.attacks = [Attack("scratch", "plant", 10, 93), Attack("papa", "fire", 30, 93)]
pikamon2.attacks = [Attack("papa", "fire", 10, 93)]
pikamon3.attacks = [Attack("scratch", "plant", 100, 93)]
pikamon4.attacks = [Attack("scratch", "plant", 100, 93)]
pikamon5.attacks = [Attack("scratch", "plant", 100, 93)]
pikamon6.attacks = [Attack("scratch", "plant", 100, 93)]

# A pelear!
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
        battle.status()
