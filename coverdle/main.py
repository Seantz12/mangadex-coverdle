import random

from blur import blur_image
from mangadex import get_random_manga, get_cover_urls

# temporary for testing
if __name__ == "__main__":
    random_manga_id = get_random_manga()
    covers = get_cover_urls(random_manga_id)

    random_cover = random.randint(0, len(covers)-1)
    blurred_cover = blur_image(covers[random_cover], 20)
    blurred_cover.show()