import lyricsgenius

# Head over to -> 'https://genius.com/api-clients/new' create a account and the generate client api and get your 'CLIENT ACCESS TOKEN'
# Input your GENIUS API : CLIENT ACCESS TOKEN
# After every 100 song fetching requests the new API client needs to be created
client_access_token = str(input("Enter the client access token : "))

# Camel Case should be ensured , example -> "Phoebe Bridgers"
name_of_artist = str(input("Enter the name of artist whose lyrics are to be saved : "))

# Number of songs 

# Very famous artists have almost 100 songs in GENIUS webite
# Medium famous artists have almost 50 songs in GENIUS website
# Not so famous artists have almost 30 songs in GENIUS website
num_of_songs = int(input("Enter the number of songs to be saved : "))

# Sort according to 'title' or 'popularity'
sorting_order = str(input("Enter the sorting order , either title or popularity : "))

genius = lyricsgenius.Genius(client_access_token)

artist = genius.search_artist(name_of_artist, max_songs = num_of_songs, sort = sorting_order)

# Saves a JSON file in the same directory containing information about all the individual songs in a single file
artist.save_lyrics()
