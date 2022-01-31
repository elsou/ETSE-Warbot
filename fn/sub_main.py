import random

from fn import build_tweet
from fn import get
from fn import instaAPI
from fn import media
from fn import storage
from fn import twitterAPI
from fn.classes import Ftext

class Fighters:
    def __init__(self, asesino, asesino2, victima, victima2):
        self.asesino = asesino
        self.asesino2 = asesino2
        self.victima = victima
        self.victima2 = victima2

def morte(info):
    players = storage.txt_to_players()

    p1 = get.p1(players)
    p2 = get.p2(players, p1)

    p1_ali = get.ali(players, p1)
    p2_ali = get.ali(players, p2)

    forza_total = p1.forza + p1_ali.forza + p2.forza + p2_ali.forza

    if random.randint(0, forza_total) < (p1.forza + p1_ali.forza):
        fighters = Fighters(p1, p1_ali, p2, p2_ali)
    else:
        fighters = Fighters(p2, p2_ali, p1, p1_ali)

    mods = storage.txt_to_mods()
    mod = get.mod(mods, fighters.victima, fighters.asesino)
    verbo = get.verbo(fighters.victima)

    media.crear_tumba(fighters, len(players))
    tweet = build_tweet.morte(fighters, mod, verbo)

    storage.update_verbos(verbo, storage.txt_to_verbos())
    storage.update_mods(mod, mods)
    storage.update_players(players, fighters)

    tweet += build_tweet.complete_tw(players)

    if len(players) == 1:
        media.update_foto('Media/ganhador.png', [])
    elif len(players) == 2 and players[0].alianza == players[1].nome:
        media.update_foto('Media/ganhador.png', [])

    return tweet


def alianza(info):
    players = storage.txt_to_players()
    p1 = players[random.randint(0, len(players) - 1)]
    r = random.randint(0, len(players) - 2)

    if r >= players.index(p1):
        r += 1
    p2 = players[r]

    if p1.alianza == 'x' and p2.alianza == 'x':
        p1.alianza = p2.nome
        p2.alianza = p1.nome
        tweet = f'[BREAKING NEWS]: {p1.nome} iniciou unha alianza con {p2.nome}'
        storage.update_players(players)
        media.update_foto('Media/foto_alianza.png', [])
    else:
        tweet = morte(info)

    return tweet


def resumo_kills():
    players = storage.txt_to_players()
    top = []

    for player in players:
        flag = 0
        i = 0
        while i < 5 and not flag:
            if len(players) > i and len(top) == i or player.kills > top[i].kills:
                top.insert(i, player)
                flag = 1
            i += 1

    tweet = ''
    for i in range(0, 5):
        if top[i].kills == 1: pl = ''
        else: pl = 's'
        if len(players) > i:
            tweet += f"#{i + 1}: {top[i].nome} ({top[i].kills} kill{pl})\n"

    texto_resumo = Ftext(text=tweet, font='Fonts/Youtube.ttf', size=55, pos=(0, 80))
    media.update_foto('Media/foto_resumo.png', [texto_resumo])

    tweet = '[TOP 5 DEATHLIEST ENGINEERS]\n' + tweet
    return tweet


def resumo_killed_1():
    killed = storage.txt_to_killed()
    tweet = '[ESQUELAS SEMANAIS] (1/2)\n'
    for i in range(0, len(killed)//2):
        tweet += f'💀 {killed[i]}\n'
    return tweet


def resumo_killed_2():
    killed = storage.txt_to_killed()
    tweet = '[ESQUELAS SEMANAIS] (2/2)\n'
    for i in range(len(killed)//2, len(killed)):
        tweet += f'💀 {killed[i]}\n'
    f = open("Storage/killed.txt", "w", encoding="ISO-8859-1")
    f.close()
    return tweet


def publish(tweet, tw, ig, disp, add_media):
    foto = 'Media/resultado.jpeg'
    print(tweet + '\n')

    if disp:
        media.display(foto)

    if tw:
        print("Publicando tweet...")
        twitterAPI.upload(tweet, foto, add_media)
        print('[completado]')
    if ig:
        print("Publicando en instagram...")
        instaAPI.upload(tweet, foto)
        print('[completado]')
