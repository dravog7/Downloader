# Downloader

Sents multiple concurrent requests of different ranges of the file to be downloaded and then combine them. Hence bypassing server side download speed limits.

## How To Use

- Run the sheduler.py

- Enter link to download

## TO-DO
- handle errors and disconnection
- handle redirection of link ('Location' header in response)
- add SQLite model and sheduler
- add resume/start to ui