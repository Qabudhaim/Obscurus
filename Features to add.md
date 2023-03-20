## 1. Saving images to media file using the following script:

```python
import requests
from PIL import Image
from io import BytesIO

# Replace with the URL of the Unsplash image you want to download
url = "https://images.unsplash.com/photo-1562408590-e32931084e23?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"

# Send a GET request to the URL to download the image
response = requests.get(url)

# Open the response content as an image using Pillow
img = Image.open(BytesIO(response.content))

# Replace with the desired filename and extension
filename = "unsplash_image.jpg"

# Save the image to the file
img.save(filename)
```

## 2. Add colors to the code fence
Use the following keywords: Pygments, Prism, codehilite

## 3. Add TOC

## 4. Add permession for deleting notes