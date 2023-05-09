import requests
from PIL import Image
from io import BytesIO
import os
from django.core.exceptions import ValidationError


def save_image_from_url(url, filename):
    response = requests.get(url)
    try:
        img = Image.open(BytesIO(response.content))
    except:
        return ValidationError("The URL is not a valid image.")
    
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)



    img.save(filename)