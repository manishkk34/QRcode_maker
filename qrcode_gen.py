import qrcode

obj = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
url = input("Enter the web link for the QR code: ")
obj.add_data(url)
obj.make(fit=True)
qr_img = obj.make_image(full_color="black", back_color="white")
qr_img.save("QR_maker.png")
