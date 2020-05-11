import deezer
import webbrowser
import random

def findGenre(mood):
    client2 = deezer.Client()
    genres = client2.get_genres()

    sad = [genres[6],genres[8],genres[10],genres[11], genres[19],genres[20],genres[22]]
    happy = [genres[1],genres[2],genres[3],genres[4], genres[5], genres[8],genres[12], genres[15]]

    if(mood == 'Sad'):
        rand = random.randint(0,len(sad)-1)
        return sad[rand]
    if(mood == 'Happy'):
        rand = random.randint(0,len(happy)-1)
        return happy[rand]

def findRandomSong(artist):
    client = deezer.Client()
    results = client.search(artist, relation = 'artist')[0]
    albums = results.get_albums()

    rand = random.randint(0, len(albums)-1)
    randAlbum = albums[rand]
    tracks = randAlbum.get_tracks()
    rand = random.randint(0, len(tracks)-1)
    randTrack = tracks[rand]
    randTrack_info = randTrack.asdict()
    print(randTrack)
    return randTrack_info['link']
    
    '''
    for album in albums:
        current_album = album 
        tracks = current_album.get_tracks()
        for track in tracks:
            current_track_info = track.asdict()
            if(current_track_info['title'] == song):
                info = track.asdict()
                print(f"Song found! {info['title']} by {track.get_artist()}")
                return info['link']
    return "Song not found"
    '''

def openBrowserForSong(mood):
    mood_genre = findGenre(mood)
    artists = mood_genre.get_artists()
    rand = random.randint(0,len(artists)-1)
    artist_object = artists[rand]
    artist_info = artist_object.asdict()

    song_link = findRandomSong(artist_info['name'])
    webbrowser.open(song_link,1)

print(openBrowserForSong('Happy'))