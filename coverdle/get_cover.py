from typing import List
import MangaDexPy


def get_cover_urls(manga_id: str) -> List[str]:
    cli = MangaDexPy.MangaDex()

    manga = cli.get_manga(manga_id)
    covers = cli.get_manga_covers(manga)
    cover_urls = []
    for cover in covers:
        cover_urls.append(cover.url)

    return cover_urls


