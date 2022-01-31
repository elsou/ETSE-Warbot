import random
from fn import storage
from fn.classes import Player, Mod

def p1(players):
    p1 = players[random.randint(0, len(players) - 1)]
    return p1

def p2(players, p1):
    if len(players) < 20:
        if p1.alianza == 'x':
            r = random.randint(0, len(players) - 2)
            if r >= players.index(p1):
                r += 1
        else:
            p1_ali = ali(players, p1)
            r = random.randint(0, len(players) - 3)
            if r >= players.index(p1):
                r += 1
            if r >= players.index(p1_ali):
                r += 1
                if r == players.index(p1):
                    r += 1
        p2 = players[r]
    else:
        p2 = players[random.randint(0, len(players) - 1)]
    return p2

def ali(players, player):
    ali = Player('x','x','x', 0,0)
    if player.alianza != 'x':
        for i in range(0, len(players)):
            if players[i].nome == player.alianza:
                ali = players[i]
    return ali

def mod(mods, victima, asesino):
    md = mods[random.randint(0, len(mods) - 1)]
    i = 0
    t = 0
    while (md.pl == '1' and (victima.alianza != 'x' or asesino.alianza != 'x')) and t==0:
        md = mods[random.randint(0, len(mods) - 1)]
        i += 1
        if i >= 10:
            md = Mod(' na aula A4', ' na aula A4', '0')
            t = 1
    return md

def verbo(victima):
    verbos = storage.txt_to_string('Storage/verbos.txt')
    verbo = verbos[random.randint(0, len(verbos) - 1)]
    return verbo

def autokill():
    autokills = storage.txt_to_string('Storage/autokills.txt')
    autokill = autokills[random.randint(0, len(autokills) - 1)]
    return autokill