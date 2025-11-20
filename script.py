import os

from PIL import Image
import requests
from io import BytesIO
from os import environ

import inky

display = inky.Inky_Impressions_7

backendurl = os.environ['BACKEND_URL']

result = requests.get(backendurl + '/refresh')

img = Image.open(BytesIO(result.content))
display.set_image(image=img, saturation=0.5)

display.show()