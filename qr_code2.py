import qrcode 
from PIL import Image
import qrcode.constants
qr= qrcode.QRcode(version=1,
                  error_connection=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4,)
qr.add_data("your link")
qr.make(fit=True)
img=qr.make_image(fill_color="code color", back_color="blue")
img.save("export file name and it format")