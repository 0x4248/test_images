import PIL
from PIL import Image

img = PIL.Image.new('RGB', (1, 1), color='white')
img.save('1pixel.png')
