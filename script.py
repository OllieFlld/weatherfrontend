from PIL import Image
import requests
from io import BytesIO

from inky.auto import auto
display = auto()


url = 'http://192.168.0.23:18080/refresh'

result = requests.get(url)

img = Image.open(BytesIO(result.content))
display.set_image(img)

display.show()