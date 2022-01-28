import qrcode
from PIL import ImageDraw

url = input("Url to transform: ")
img = qrcode.make(url)
ImageDraw.Draw(img).text((5, 5), url)
img.show()
