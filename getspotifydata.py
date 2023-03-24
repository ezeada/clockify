# a script to recreate the spotify dataset because theyre taking 30 days to send me mine 

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
from pandas import read_csv
CLIENT_ID = ''
CLIENT_SECRET = ''


client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# open csv
df = read_csv('borisstation/4-borisstation (1).csv')

to_drop = []

id, acousticness, danceability, energy, tempo, valence, loudness, instrumentalness, speechiness = [], [], [], [], [], [], [], [], []
count = 0

for ind in df.index:
    # get track id
    currid = sp.search(q = "track:" + df.loc[ind, 'Track'] + " artist:" + df.loc[ind, 'Artist'], limit=1, type='track')
    if currid['tracks']['items'] != []:
        if currid['tracks']['items'][0] != None:
            id.append(currid['tracks']['items'][0]['id'])
            features = sp.audio_features(tracks=id[count])
            # get track features (read more @ https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features)
            acousticness.append(features[0]["acousticness"])
            danceability.append(features[0]["danceability"]) #0 to 1
            energy.append(features[0]["energy"]) #0 to 1
            tempo.append(features[0]["tempo"]) #int
            valence.append(features[0]["valence"])
            loudness.append(features[0]["loudness"]) # -60 to 0 dB
            instrumentalness.append(features[0]["instrumentalness"]) #0 to 1
            speechiness.append(features[0]["speechiness"])

            count += 1
            time.sleep(1)
        else:
            print(df.loc[ind, 'Track'])
            to_drop.append(ind)
    else:
        print(df.loc[ind, 'Track'])
        to_drop.append(ind)
    print(ind) # for tracking purposes
    
df = df.drop(to_drop)

df['acousticness'] = acousticness
df['danceability'] = danceability
df['energy'] = energy
df['tempo'] = tempo
df['valence'] = valence
df['loudness'] = loudness
df['instrumentalness'] = instrumentalness
df['speechiness'] = speechiness


df.to_csv("borisstation/4-borisstation new.csv", index=False)
