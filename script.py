import os

from PIL import Image
import requests
from io import BytesIO
from os import environ

from inky import InkyE673
display = InkyE673(ask_user=True, verbose=True)

backendurl = os.environ['BACKEND_URL']

result = requests.get(backendurl + '/refresh')

img = Image.open(BytesIO(result.content))
display.set_image(image=img)

display.show()