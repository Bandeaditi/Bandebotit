import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set your Spotify API credentials
spotify_client_id = ''
spotify_client_secret = ''

# Authenticate with the Spotify API using your credentials
client_credentials_manager = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to search for a song by its name
def search_song_by_name(song_name):
    results = sp.search(q=song_name, type="track", limit=1)
    if 'tracks' in results and results['tracks']['items']:
        track = results['tracks']['items'][0]
        popularity = track['popularity']
        return f"Song: {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}\nAlbum: {track['album']['name']}\nPopularity: {popularity}\nSpotify URL: {track['external_urls']['spotify']}"
    else:
        return "Song not found with the given name."

# Input the song name to search for
song_name = input("Enter the song name: ")
result = search_song_by_name(song_name)
print(result)
