# Spotify ETL

A Python script that exports all of your Spotify playlists and produce an analysis of the music that you are currently listening.

## Authors

- Jason H.

- Kun Z.

- Pierre-Olivier B.

## Resources

> Run: python api/main.py

### Venv

> python3 -m venv env

> source env/bin/activate

> cd api && export AIRFLOW_HOME=$PWD

> pip install -r requirements.txt (To generate one: pip freeze > requirements.txt)

> airflow db init

> airflow scheduler

> airflow webserver

Generate a txt: pip freeze > requirements.txt

### Airflow

> airflow webserver -p 8080

> http://localhost:8080/

User - pass: admin - admin1234

### References

## Spotify Official

- https://developer.spotify.com/discover/

### API

- https://developer.spotify.com/documentation/general/guides/authorization-guide/

- https://github.com/caseychu/spotify-backup

- https://github.com/btk-dev/recentlyPlayedSongsSpotify/blob/master/apilayer.py

#### Generate Token Manually

- https://developer.spotify.com/console/get-playlists/

## ML

https://m.youtube.com/watch?v=EbPYpTcATPg&feature=youtu.be

### NLP - Timeseries

- PyCaret - TS: https://towardsdatascience.com/multiple-time-series-forecasting-with-pycaret-bc0a779a22fe

## Frontend

- NextJS

### ETL

- Youtube Part 1,2,3

[Schema] + [DB Schema]

### Scheduler - Airflow

Airflow 15 min video
