#!/usr/bin/python3

import requests
import spotipy.util as util
from my_secrets import *

# Generates Auth Token from Secrets

def generate_token(client_id: str, client_secret: str) -> str:
    
    # Set up preferences
    scope = "user-read-recently-played"
    redirect_uri = "http://localhost:7777/callback"

    return util.prompt_for_user_token(username=username, 
                                      scope=scope, 
                                      client_id=client_id, 
                                      client_secret=client_secret,
                                      redirect_uri=redirect_uri)


# GET Request to JSON (dict)

def grab_json_from_url(url: str, token: str) -> dict:
    headers = {
        'Authorization': f'Bearer {token}'
    }
    resp = requests.get(url, headers=headers)
    return resp.json()


# Gets the most recent track from recent_plays

def get_recent_track_id(recent_plays: dict) -> str:
    return recent_plays['items'][0]['track']['id']


def main():
    token = generate_token(client_id, client_secret)
    recent_plays = grab_json_from_url('https://api.spotify.com/v1/me/player/recently-played', token)
    id = get_recent_track_id(recent_plays)
    print(id)

if __name__ == "__main__":
    main()