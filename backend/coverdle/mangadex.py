import json
import requests
import MangaDexPy

from typing import List


# Takes in parameters for random search, then returns manga id
# or maybe i should make it return a manga object? decisions...
def get_random_manga(content_ratings: list = ["safe"]) -> str:
    # because the python library hasn't implemented this yet, gotta do this myself
    endpoint = "https://api.mangadex.org/manga/random"
    payload = {
        "contentRating[]": content_ratings,
    }
    response = json.loads(requests.get(endpoint, params=payload).text)
    return response["data"]["id"]


def get_cover_urls(manga_id: str) -> List[str]:
    cli = MangaDexPy.MangaDex()

    manga = cli.get_manga(manga_id)
    covers = cli.get_manga_covers(manga)
    cover_urls = []
    for cover in covers:
        cover_urls.append(cover.url)

    return cover_urls


