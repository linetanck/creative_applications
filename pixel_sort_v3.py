from pixelsort import pixelsort
from PIL import Image
a = Image.open("sunset.jpg")
a = pixelsort(a)
a.show()

