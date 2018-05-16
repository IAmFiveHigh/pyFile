import pyqrcode
import os


a = input("输入生成二维码的内容")
b = os.path.abspath(".")

qr = pyqrcode.create(a)

qr.png("{}/Desktop/二维码.png".format(b), scale=10)

