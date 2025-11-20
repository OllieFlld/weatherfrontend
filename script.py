import os

from PIL import Image
import requests
from io import BytesIO
from os import environ

from inky import InkyE673
display = InkyE673()

backendurl = os.environ['BACKEND_URL']

result = requests.get(backendurl + '/refresh')

img = Image.open(BytesIO(result.content))
display.set_image(img)

display.show()