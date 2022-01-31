import random

# Representa un xogador
class Player:
    def __init__(self, nome='x', pronome='x', alianza='x', kills=0, forza=0):
        self.nome = nome
        self.pronome = pronome
        self.alianza = alianza
        self.kills = kills
        self.forza = forza

# Representa un modificador
class Mod:
    def __init__(self, masc, fem, pl):
        self.masc = masc
        self.fem = fem
        self.pl = pl

# Contén a información requerida para fusionar un texto cunha imaxe (str text, str font, int size, (int, int) pos)
class Ftext:
    def __init__(self, text, font, size, pos):
        self.text = text
        self.font = font
        self.size = size
        self.pos = pos
