from fn.sub_main import morte, alianza, resumo_kills, resumo_killed_1, resumo_killed_2, publish
from fn import storage
import random

incremento = 17
prob_alianzas = 1
limite_alianzas = 20
info = False
display_fotos = True
post_on_tw = False
post_on_ig = False

storage.reset(False)

days = storage.read_day()
print(f"Día {days}:")

if days % 7 == 0 and days != 0:
    if info: print('RESUMO:')
    tweet = resumo_killed_1()
    publish(tweet, tw=post_on_tw, ig=post_on_ig, disp=display_fotos, add_media = False)
    tweet = resumo_killed_2()
    publish(tweet, tw=post_on_tw, ig=post_on_ig, disp=display_fotos, add_media = False)
    tweet = resumo_kills()
    publish(tweet, tw=post_on_tw, ig=post_on_ig, disp=display_fotos, add_media = True)
else:
    n_players = len(storage.txt_to_players())
    last = n_players <= 5
    for i in range(0, 3-last*2):
        if random.randint(0, prob_alianzas) < 1 and n_players > limite_alianzas:
            if info: print('ALIANZA:')
            tweet = alianza(info)
        else:
            if info: print('MORTE:')
            tweet = morte(info)
        publish(tweet, tw=post_on_tw, ig=post_on_ig, disp=display_fotos, add_media = True)

storage.add_day(days)
