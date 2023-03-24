import requests
from PIL import Image
from io import BytesIO
import os

def save_image_from_url(url, filename):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)



    img.save(filename)