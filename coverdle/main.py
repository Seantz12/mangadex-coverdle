from blur import blur_image
from get_cover import get_cover_urls

# temporary for testing
if __name__ == "__main__":
    covers = get_cover_urls("b9797c5b-642e-44d9-ac40-8b31b9ae110a")
    blurred_covers = []
    for cover in covers:
        blurred_image = blur_image(cover, 5)
        blurred_covers.append(blurred_image)

    blurred_covers[0].show()