import requests
import json
from credentials import mangadex_credentials

# Mangadex
mangadex_url = "https://api.mangadex.org"

# Authenticate account to access Mangadex
r = requests.post(
    "https://auth.mangadex.org/realms/mangadex/protocol/openid-connect/token",
    data=mangadex_credentials
)
r_json = r.json()

access_token = r_json["access_token"]
refresh_token = r_json["refresh_token"]

# Search for specific manga
# Ex. "Hikagemono demo Yarinaoshite Ii desu ka?"
# title = "Hikagemono demo Yarinaoshite Ii desu ka?"
# rating = 10

title = input("Enter Manga to rate: ")
rating = int(input("Enter your rating: "))

r = requests.get(
    f"{mangadex_url}/manga",
    params={"title": title}
)
r_json = r.json()

mangadex_manga_id = r_json["data"][0]["id"]
mangadex_rating_payload = {"rating": rating}

# Post rating to Mangadex
r = requests.post(
    f"{mangadex_url}/rating/{mangadex_manga_id}",
    headers={"Authorization": f"Bearer {access_token}"},
    json=mangadex_rating_payload
)
r_json = r.json()

# TODO: MyAnimeList


# TODO: AniList
