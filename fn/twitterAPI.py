import tweepy

# Claves para o acceso á API de twitter
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

# # Dado un tweet (str) e imaxe (str '*.jpeg'), publica o contido en twitter
def upload(tweet, imaxe, add_media):
    oauth = OAuth()
    api = tweepy.API(oauth)
    media = api.media_upload(imaxe)
    if add_media:
        api.update_status(status=tweet, media_ids=[media.media_id])
    else:
        api.update_status(status=tweet)

# Autentica as claves establecidas
def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None
