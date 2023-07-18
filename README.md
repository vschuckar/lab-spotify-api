![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Extending the internal databases with audio features

At this point, you have the **hot_songs** and the **not_hot_songs** databases. However, you don't have any acoustic information about the songs. 
The purpose of this lab is to use Spotify's API to extend both databases with this information for each song included to use this information later.

# Instructions

* Create a function to search a given **single** song in the Spotify API: **search_song(title, artist)**. 

Take into account that sometimes Spotify's API will return several matches for the same song title (different artists, a different album of the same artist, version of the song,...etc). Then it will be nice to display a list of outputs to the user and let him/her select which is the right match. Once the desired song is located, the function should return the href/id/uri of the song to the code (not to the user).
Keep in mind, that a given song might not be available on Spotify's API (make sure to use the song's title and artist searching the song). If the song is not found, the function must return an empty string as the href/id/uri. Also, in this case, you should remove this song from the database.

* Create a function **get_audio_features(list_of_song_ids)** to obtain the audio features of a given list of songs (the content of list_of_songs can be the href/id/uri). 

Be careful to not exceed the number of calls to the API otherwise, you will be banned and you will have to wait several hours before launching a new request [see here](https://developer.spotify.com/documentation/web-api/guides/rate-limits/).
A good strategy to prevent this problem is to split the list of song id's in "chunks" of 50 songs id's and wait 20 seconds before asking for the audio features of the next "chunk".
Then, use this function to create a Pandas Dataframe with the audio features of the list of songs. Hint: create a dictionary with the song's audio features as keys and an **empty list as values**. 
Then fill in the lists with the corresponding audio features of each song. Finally, create your data frame from the dictionary.

* Once the previous function has been created, create another function **add_audio_features(df, audio_features_df)** to concat a given dataframe with the dataframe containing the audio features alongside any other desired info, and return the extended data frame.
Replace the old internal files of songs (hot and not hot) with the extended data frames with the audio features and save them into separate files on the disk.
