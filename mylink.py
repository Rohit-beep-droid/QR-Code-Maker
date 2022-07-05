import qrcode
from PIL import Image, ImageDraw
img = qrcode.make('https://www.linkedin.com/in/rohit-barua/')
img.save('MyLinkedInQRCode.jpg')