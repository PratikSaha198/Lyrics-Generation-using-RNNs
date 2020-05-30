import lyricsgenius
import json
import re

# Camel Case should be ensured , example -> "Phoebe Bridgers"
num_of_artists = int(input("Enter the number of artist whose lyrics are to be saved : "))

Artists = []

for i in range(num_of_artists):
	name = str(input("Name of artist : "))
	Artists.append(name)

# Scrapping / Extracting the lyrics from all the JSON files saved in the root directory after running 'lyrics_scapper_from_GENIUS_website.py' as many times

total_all_lyrics_big_string = ''

names_of_all_artists_files = []

# Getting the names of the files
for name in Artists :
	name_removed_spaces = name.replace(' ' , '')
	name_colagulated = name_removed_spaces.replace('&' , '')
	final_name = 'Lyrics_' + name_colagulated + '.json'
	names_of_all_artists_files.append(final_name)

# Scaraping the lyrics from JSON and a little processing
for name in names_of_all_artists_files :
	jsonFile = open(name , 'r')
	values = json.load(jsonFile)
	jsonFile.close()
	for song_data in values['songs']:
		individual_lyrics = str(song_data['lyrics'])
		individual_lyrics = re.sub('(\[.*?\])*','', individual_lyrics)
		total_all_lyrics_big_string = total_all_lyrics_big_string + individual_lyrics

# print(total_all_lyrics_big_string)

# Saving all lyrics in a text file in the same directory with the name 'lyrics_dataset.txt'
lyrics_dataset = open("lyrics_dataset.txt","w+",encoding='utf8')
lyrics_dataset.write(total_all_lyrics_big_string)
lyrics_dataset.close()

print()
print("lyrics_dataset.txt saved in the same directory")