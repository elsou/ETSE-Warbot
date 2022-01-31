import tweepy

# Claves para o acceso á API de twitter
consumer_key = 'Flht3DoIWkfYaHr3FO3HG9SpW'
consumer_secret = 'WrWSFa9Hc9psXJYwOFMQc8xLVSj89TP4TNPXodtGziiPeKx64o'
access_token = '1301652464098254850-dWRE4GCBnVuApsPPos2BPlxVXnA2QO'
access_token_secret = 'kwq3niNK4C1AbcE4k8LHpXrM33PcyNxdayuG04YwnxHOY'

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