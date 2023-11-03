import qrcode

class dokkaebi_QR_generator:
    def __init__(self):
        self.qr_data = None
        self.qr_img = None
        self.savePath = None

    def genQRCode(self,data):
        self.qr_data = data
        self.qr_img = qrcode.make(self.qr_data)
        self.savePath = self.qr_data +'.png'
        self.qr_img.save(self.savePath)
