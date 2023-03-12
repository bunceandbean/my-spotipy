#!/usr/bin/python3

import json
import requests

def grab_json_from_url(url: str) -> dict:
    token = ""
    headers = {
        'Authorization': f'Bearer {token}'
    }
    resp = requests.get(url, headers=headers)
    return resp.json()

def main():
    my_json = grab_json_from_url('https://api.spotify.com/v1/me/player/recently-played')
    print(my_json['items']) #[~0]['track']['id']
    for item in my_json['items']:
        print(item['track']['name'], item['played_at'])

if __name__ == "__main__":
    main()