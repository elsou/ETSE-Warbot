from PIL import Image, ImageFont, ImageDraw
from datetime import date
from fn.classes import Ftext

# A data actual
hoxe = date.today().strftime("%d/%m/%Y")


# Dada a dirección a unha foto de fondo e un array de obxectos Ftext,
# garda a combinación de todos en "Media/resultado.jpeg"
def update_foto(background, ftextos):
    bkg = Image.open(background).convert("RGBA")
    texto_img = Image.new('RGBA', bkg.size, (255, 255, 255, 0))
    edicion = ImageDraw.Draw(texto_img)
    for ftxt in ftextos:
        add_text(ftxt, edicion, img_width=bkg.size[0], centered=True)
    edicion_final = Image.alpha_composite(bkg, texto_img).convert("RGB")
    edicion_final.save("Media/resultado.jpeg")


# Crea a imaxe da tumba individual/dobre cos nomes das víctimas e gárdaa en "Media/resultado.jpeg"
def crear_tumba(fighters, posto):
    victima = fighters.victima
    victima2 = fighters.victima2
    if victima2.nome != 'x':
        if victima.pronome == victima2.pronome:
            subtexto = f'Falecid{victima.pronome}s o ' + hoxe
        else:
            subtexto = f'Falecides o ' + hoxe

        fnome = Ftext(text=victima.nome + ' e ' + victima2.nome, font='Fonts/Cormorant.ttf', size=62, pos=(0, 340))
        fsubtexto = Ftext(text=subtexto, font='Fonts/Cormorant.ttf', size=50, pos=(0, 410))
        fkills = Ftext(text=f'K: {victima.kills}', font='Fonts/Futura.ttf', size=55, pos=(-295, 120))
        fkills2 = Ftext(text=f'K: {victima2.kills}', font='Fonts/Futura.ttf', size=55, pos=(365, 120))
        fposto = Ftext(text=f'#{posto}', font='Fonts/Futura.ttf', size=55, pos=(-10, 125))

        update_foto('Media/foto_morte_dobre.png', [fnome, fsubtexto, fkills, fkills2, fposto])

    else:
        fnome = Ftext(text=victima.nome, font='Fonts/Cormorant.ttf', size=65, pos=(0, 265))
        fsubtexto = Ftext(text=f'Falecid{victima.pronome} o ' + hoxe, font='Fonts/Cormorant.ttf', size=55, pos=(0, 355))
        fkills = Ftext(text=f'K: {victima.kills}', font='Fonts/Futura.ttf', size=55, pos=(165, 120))
        fposto = Ftext(text=f'#{posto}', font='Fonts/Futura.ttf', size=55, pos=(-185, 125))

        update_foto('Media/foto_morte.png', [fnome, fsubtexto, fkills, fposto])

# Engade un texto dado a unha edición dunha imaxe
def add_text(ftxt, img, img_width, centered):
    fonte = ImageFont.truetype(ftxt.font, ftxt.size)
    if centered:
        pos = (img_width / 2 - ancho(ftxt.text, fonte) // 2 + ftxt.pos[0], ftxt.pos[1])
    else:
        pos = ftxt.pos
    img.text(pos, ftxt.text, fill=(50, 50, 50, 110), font=fonte)


# Dado un texto e unha fonte de PIL (ImageFont.truetype(font, size) devolve o seu ancho en pixeles
def ancho(text, font):
    im1 = Image.new('RGBA', (1000, 1000), (255, 255, 255, 0))
    img = ImageDraw.Draw(im1)
    fonte = font
    w = img.textsize(text, font=fonte)[0]
    return w


# Dada unha dirección a unha fotografía móstraa en pantalla (nunha nova lapela)
def display(foto):
    image = Image.open(foto)
    image.show()
