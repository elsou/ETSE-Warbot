from instabot import Bot
import os
import shutil
import time

# Dado un tweet (str) e imaxe (str '*.jpeg'), publica o contido en instagram
def upload(tweet, imaxe):
    clean_up()
    bot = Bot()
    bot.login(username="usename", password="password")
    time.sleep(1)
    bot.upload_photo(imaxe, caption=tweet)

# ...
def clean_up():
    dir = "../config"
    remove_me = "imgs\img.jpg.REMOVE_ME"
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("imgs\img.jpg")
        os.rename(remove_me, src)





