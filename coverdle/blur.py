from PIL import Image, ImageFilter
import requests

def get_image_from_url(url: str) -> Image:
    image_data = requests.get(url, stream=True).raw
    image_object = Image.open(image_data)

    return image_object

def blur_image(url: str, blur_amount: int) -> Image:
    image = get_image_from_url(url)

    blurred_image = image.filter(ImageFilter.BoxBlur(blur_amount))
    return blurred_image
