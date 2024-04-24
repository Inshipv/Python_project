import qrcode
from PIL import Image

qr =qrcode.QRCode(version = 1 , error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 30,border =3)

qr.add_data("https://www.google.com")
qr.make(fit = True)
img = qr.make_image(fill_color = "red", back_color = "white",)
img.save("google.png")