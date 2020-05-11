import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
cid = ''
secret = 'a3ec441956fa4b6f8bc768df96bfda1d'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []
track_genre = []
for i in range(0,1):
    track_results = sp.search(q='year:2018', type='track', limit=1,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        if(i == 0):
            print(type(t))
            print(t.keys())
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
        track_genre.append(t['album'])
print(artist_name)
print(type(artist_name))
print(track_name)
print(type(track_name))
print(popularity)
print(type(popularity))
print(track_id)
print()
#print(track_genre)
#print(type(track_genre))
print(type(track_genre[0]))
print(track_genre[0].keys())#This is the album info
print(track_genre[0]['href'])