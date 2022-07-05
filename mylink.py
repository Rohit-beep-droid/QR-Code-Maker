# Must have QR code installed for this code to function
import qrcode
from PIL import Image, ImageDraw

img = qrcode.make('add your link')
img.save('name of the qr code image created')
