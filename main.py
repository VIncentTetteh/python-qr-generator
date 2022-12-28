import qrcode

from PIL import Image

qr = qrcode.QRCode(version=1.0,error_correction=qrcode.ERROR_CORRECT_H,box_size=15, border=5)

qr.add_data("www.amazon.com")

qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="blue")
img.save("Amazon.png")
