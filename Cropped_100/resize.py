cropped = open("cropped.jpg", "rb").read()

uncropped = cropped.replace("\x01\xc2\x01\x82", "\x02\xc2\x01\x82")

open("uncropped.jpg", "w").write(uncropped)
