# build_tweet.py #
from fn import get

def morte(fighters, mod_, verbo_):
    tweet = ''
    asesino = fighters.asesino
    victima = fighters.victima
    victima2 = fighters.victima2
    autokill = get.autokill()
    verbo = verbo_.replace('*', victima.pronome)
    if victima.kills > 1: pl = 's'
    else: pl = ''
    if victima.kills > 0: kills1 = f' ({victima.kills} kill{pl})'
    else: kills1 = ''

    if victima2.kills > 1: pl = 's'
    else: pl = ''
    if victima2.kills > 0: kills2 = f' ({victima2.kills} kill{pl})'
    else: kills2 = ''

    if victima.pronome == 'a': mod = mod_.fem
    else: mod = mod_.masc

    if asesino.nome != victima.nome and asesino.nome != victima.alianza and asesino.alianza != victima.nome:
        if asesino.alianza == 'x' and victima.alianza == 'x':
            tweet = f'[BREAKING NEWS]: {asesino.nome} {verbo} a {victima.nome}{kills1}{mod}\n'

        elif asesino.alianza != 'x' and victima.alianza != 'x':
            tweet = f'[BREAKING NEWS]: {asesino.nome} e {asesino.alianza} asesinaron a ' \
                    f'{victima.nome}{kills1} e ' \
                    f'{victima2.nome}{kills2}{mod}\n'

        elif asesino.alianza != 'x':
            tweet = f'[BREAKING NEWS]: {asesino.nome} e {asesino.alianza} asesinaron a {victima.nome}{kills1}{mod}.\n'

        elif victima.alianza != 'x':
            tweet = f'[BREAKING NEWS]: {asesino.nome} matou a {victima.nome}{kills1} ' \
                    f'e {victima2.nome}{kills2}{mod}\n'

    elif asesino.nome == victima.nome:
        tweet = f'[BREAKING NEWS]: {victima.nome} {autokill}.\n'

    else:
        tweet = f'[BREAKING NEWS]: {asesino.nome} traicionou a {victima.nome}{kills1}{mod}\n'

    return tweet

def complete_tw(players):
    if len(players) == 1:
        extra = f'{players[0].nome} gaña os I xogos da ETSE\n'
    elif len(players) == 2 and players[0].alianza == players[1].nome:
        extra = f'{players[0].nome} e {players[1].nome} gañan os I xogos da ETSE\n'

    else:
        extra = f'Quedan {len(players)} superviventes'
    return extra
