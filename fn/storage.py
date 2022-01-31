import shutil
import random
from fn.classes import Player, Mod

def txt_to_players():
    f = open('Storage/nomes.txt', 'r', encoding="ISO-8859-1")
    file = f.readlines()
    players = []
    i = 0
    while i < len(file):
        player_str = file[i].split('/')
        players.append(Player(player_str[0], player_str[1],
                              player_str[2], int(player_str[3]),
                              int(player_str[4])))
        i += 1
    f.close()
    return players


def txt_to_killed():
    f = open('Storage/killed.txt', 'r', encoding="ISO-8859-1")
    file = f.readlines()
    killed = []
    i = 0
    while i < len(file):
        player_str = file[i].split('/')
        killed.append(player_str[0])
        i += 1
    f.close()
    return killed


def txt_to_mods():
    f = open('Storage/mods.txt', 'r', encoding="ISO-8859-1")
    file = f.readlines()
    mods = []
    i = 0
    while i < len(file):
        mod_str = file[i].split('/')
        mods.append(Mod(mod_str[0], mod_str[1], mod_str[2]))
        i += 1
    f.close()
    return mods


def txt_to_verbos():
    f = open('Storage/verbos.txt', 'r', encoding="ISO-8859-1")
    file = f.readlines()
    verbos = []
    i = 0
    while i < len(file):
        verbos.append(file[i])
        i += 1
    f.close()
    return verbos


def txt_to_string(arquivo):
    f = open(arquivo, 'r', encoding="ISO-8859-1")
    file = f.readlines()
    verbos = []
    i = 0
    while i < len(file):
        verb_str = file[i].split('/')
        verbos.append(verb_str[0])
        i += 1
    f.close()
    return verbos

# Dada unha lista de xogadores e uns asesinos e víctimas, actualiza o arquivo nomes.txt para o seguinte día
def update_players(players, fighters=None):
    if fighters is not None:
        victima = fighters.victima
        victima2 = fighters.victima2
        asesino = fighters.asesino
        asesino2 = fighters.asesino2

        if asesino.nome != 'x':
            if asesino2.nome != 'x':
                asesino.kills += 1
                asesino.forza += 20
                asesino2.forza += 7
            else:
                asesino.kills += 1
                asesino.forza += 20

        if asesino.alianza == victima.nome:
            asesino.alianza = 'x'

        f = open("Storage/killed.txt", "a", encoding="ISO-8859-1")
        if victima.nome != 'x':
            f.write(f"{victima.nome}/{victima.pronome}/{victima.alianza}/{victima.kills}/{int(victima.forza)}\n")
            players.remove(victima)
        if victima2.nome != 'x' and victima2.nome != asesino.nome:
            f.write(f"{victima2.nome}/{victima2.pronome}/{victima2.alianza}/{victima2.kills}/{int(victima2.forza)}\n")
            players.remove(victima2)

        f.close()

    random.shuffle(players)
    f = open("Storage/nomes.txt", "w", encoding="ISO-8859-1")
    for i in range(0, len(players)):
        f.write(f"{players[i].nome}/{players[i].pronome}/{players[i].alianza}/{players[i].kills}/{int(players[i].forza)}\n")
    f.close()

# Dada unha lista de xogadores e uns asesinos e víctimas, actualiza o arquivo nomes.txt para o seguinte día
def update_mods(mod, mods):
    mods.remove(mod)
    f = open("Storage/mods.txt", "w", encoding="ISO-8859-1")
    for i in range(0, len(mods)):
        f.write(f'{mods[i].masc}/{mods[i].fem}/{mods[i].pl}/\n')
    f.close()


def update_verbos(verbo, verbos):
    if f'{verbo}/\n' in verbos:
        verbos.remove(f'{verbo}/\n')
    else:
        verbos.remove(f'{verbo}/')
    f = open("Storage/verbos.txt", "w", encoding="ISO-8859-1")
    for i in range(0, len(verbos)):
        f.write(verbos[i])
    f.close()


def read_day():
    f = open("Storage/days.txt", "r")
    days = int(f.readlines()[0])
    f.close
    return days


def add_day(days):
    f = open("Storage/days.txt", "w", encoding="ISO-8859-1")
    days += 1
    f.write(str(days))
    f.close


def reset(on):
    if on:
        f = open("Storage/days.txt", "w", encoding="ISO-8859-1")
        f.write('1')
        f.close
        f = open("Storage/killed.txt", "w", encoding="ISO-8859-1")
        f.close()
        shutil.copyfile('Storage/nomes_ref.txt', 'Storage/nomes.txt')
        shutil.copyfile('Storage/mods_ref.txt', 'Storage/mods.txt')
        shutil.copyfile('Storage/verbos_ref.txt', 'Storage/verbos.txt')
