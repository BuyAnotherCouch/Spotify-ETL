from typing import Mapping
from pandas.core.series import Series
import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
import datetime
import sqlite3

# Token taken from https://developer.spotify.com/console/get-recently-played/

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "level_bastard"
TOKEN = "BQBIPEMta7R7GSLHd4yEPLsQcfqmyumh61HJCThybf-2uzZ-dJsg6E9wjqorK_h5WzfFu0P8ZEGORkldXEGwQ5OT5pb7JI4oqaQQI7BQsBfpdqaDI8AaXDXEe0jPjD-goxnE6LhfJ9yqitWi-H-I4TcJ"

def check_data(df: pd.DataFrame) -> bool:
    #Check if the dataframe is empty
    if df.empty:
        print("No songs downloaded. Finishing execution.")
        return False

    # Primary Key Check
    if pd.Series(df["played_at"]).is_unique:
        pass
    else:
        raise Exception("Duplicates Detected!")

    # Check for nulls
    if df.isnull().values.any():
        raise Exception("Null value found")

    # Check that all timestamps are from the previous day.
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second= 0, microsecond= 0)

    timestamps = df["timestamp"].tolist()
    for timestamp  in timestamps:
        if datetime.datetime.strptime(timestamp, "%Y-%m-%d") != yesterday:
            raise Exception("At least one of the returned songs does not come from within the last 24 hours")
# Extract
if __name__ == "__main__":
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time = yesterday_unix_timestamp), headers=headers)

    data = r.json()

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []
    album_type = []
    release_date = []

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])
        album_type.append(song["track"]["album"]["album_type"])
        release_date.append(song["track"]["album"]["release_date"])

    song_dict = {
        "song_name" : song_names,
        "artist_name" : artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps,
        "album_type" : album_type,
        "release_date" : release_date
    }

    song_df = pd.DataFrame(song_dict, columns= ["song_name", "artist_name", "played_at", "timestamp", "album_type", "release_date"])

# Validate
if check_data(song_df):
    print("Data valid, proceed to Load stage")