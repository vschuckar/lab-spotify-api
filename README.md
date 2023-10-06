![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Extending the internal databases with audio features

At this point, you have the **hot_songs** and the **not_hot_songs** databases. However, you don't have any acoustic information about the songs. 
The purpose of this lab is to use Spotify's API to extend both databases with this information to use it later.

# Instructions

* Create a function to search a given **single** song in the Spotify API: **search_song(title, artist, limit)**. 

Later, you can will use this function in the song recommender to get the audio features of each song in the database (considering only the first match, even though it might not be the best match because your time is limited and you can spend time determining the best match for each song). Keep in mind, that a given song might not be available on Spotify's API (make sure to use the song's title and artist searching the song). If the song is not found, the function must return an empty string as the href/id/uri. Also, in this case, you should remove this song from the database. You should consider using a try: except: clause like:

```python
def search_song(title, artist, limit):
  ...

list_of_ids = []
try:
  id = search_song(title, artist, limit)
  list_of_ids.append(id)
except:
  print("Song not found!")
  list_of_ids.append("")

df["id"] = list_of_ids

# Code to remove songs without IDs from the databases.
```

On the other hand, you can also use this function in the song recommender to search for the **user's song ID** in the Spotify API. However, this time you want to make sure that you get the right match. Therefore, you would like to create dataframe with a list of five matches, present them to the user, and let him select the right one like:

|   | Title | Artist |
|---|--------|-------|
| 0 | Giorgia on My Mind | Carmichaels |
| 1 | Giorgia on My Mind | Ray Charles |

Once the desired song is located, **the function should return the href/id/uri of the song to the code** (not to the user) to get the audio features.

* Create a function **get_audio_features(list_of_song_ids)** to obtain the audio features of a given list of songs (the content of list_of_songs can be the href/id/uri or a list with a single song IDs). 

Be careful to not exceed the number of calls to the API otherwise, you will be banned and you will have to wait several hours before launching a new request [see here](https://developer.spotify.com/documentation/web-api/guides/rate-limits/).

A good strategy to prevent this problem is to split the list of song IDs into "chunks" of 50 song IDs and wait 20 seconds before asking for the audio features of the next "chunk" (for your own peace of mind add a "print("Collecting IDs for chunk...") message to show the progress). To create chunks of song IDs consider using [np.split](https://numpy.org/doc/stable/reference/generated/numpy.split.html)

Then, use this function to create a Pandas Dataframe with the audio features of all the songs in the databases. Hint: create a dictionary with the song's audio features as keys and an **empty list as values**. Then, fill in the lists with the corresponding audio features of each song. Finally, create a data frame with the audio features from the dictionary.

* Once the previous function has been created, create another function **add_audio_features(df, audio_features_df)** to concat a given dataframe with the audio features dataframe and return the extended data frame.

* Finally, replace the old internal files of songs (hot and not hot) with the extended data frames with the audio features and save them into separate files on the disk.

* Remember to store your functions inside a "functions.py" library in order to be used by your final song recommender.
