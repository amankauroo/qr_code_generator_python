import qrcode
from PIL import Image

qr_data = input("Enter data: ")
qr_background_color = input("what color would you like the background to be: ")
qr_fill_color = input("what color do you want the qr code to be:  ")
qr_file_name = input("how to save your file: ")
qr_file_name_and_extension = qr_file_name + ".png"

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(qr_data)
qr.make(fit=True)
img = qr.make_image(fill_color=qr_fill_color, back_color=qr_background_color)
img.save(qr_file_name_and_extension)
