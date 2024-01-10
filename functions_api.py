
import pandas as pd
from time import sleep
import numpy as np
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from config import *

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=Client_ID,
                                                           client_secret=Client_Secret))

def search_song(title, artist, limit = 1):
    '''
    Function to search a given single song in the Spotify API. 
    Input: title = song name, artist = song singer
    Output: song id from Spotify
    '''
    
    search_query = f"track:{title} artist:{artist}"
    id = sp.search(q = search_query, limit = limit)['tracks']['items'][0]['id']
    return id 

def add_id(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Function to obtain the IDs of a given list of songs through the Spotify API.
    Input: pd.DataFrame
    Output: pd.DataFrae with the column "id" for each song
    Chunks used in order to prevent reaching the API request limit 
    '''
    
    chunks = 50
    list_of_ids = []

    for i in range(0, len(df), chunks):
        chunk = df.iloc[i:i+chunks]
        print("Collecting IDs for chunk...")
    
        for index, row in chunk.iterrows():
            title = row["title"]
            artist = row["artist"]
            try:
                id = search_song(title, artist, 1)
                list_of_ids.append(id)
            except:
                print("Song not found!")
                list_of_ids.append("")
        sleep(20)
        print("Sleep...")

    df["id"] = list_of_ids
    return df

def get_audio_features(list_of_ids: list) -> pd.DataFrame:
    '''
    Function to obtain the audio features of a given list of songs 
    Input: List with the song ids 
    Output: pd.DataFrame with the audio features for each id
    Chunks used in order to prevent reaching the API request limit
    '''
    
    chunks = 50
    audio_features = []

    for i in range(0, len(list_of_ids), chunks):
        chunk_ids = list_of_ids[i:i+chunks]
        try:
            features_chunk = sp.audio_features(tracks = chunk_ids)
            if features_chunk:
                audio_features.extend(features_chunk)  
        except:
                print("Error retrieving audio features for chunk!")
                
        sleep(20)
        print("Sleep...")
        
    audio_features = [af for af in audio_features if af is not None]
    audio_features_df = pd.DataFrame(audio_features)

    return audio_features_df

def add_audio_features(df: pd.DataFrame, audio_features_df: pd.DataFrame, key_column) -> pd.DataFrame:
    '''
    Function to merge the original df with the created df which has the song features.
    Input: df: pd.DataFrame -> original df, audio_features_df and the column on which both will merge 
    Output: The merged dataframe from the input ones
    '''

    merged_df = pd.merge(df, audio_features_df, how = 'inner', on = key_column)
    return merged_df
