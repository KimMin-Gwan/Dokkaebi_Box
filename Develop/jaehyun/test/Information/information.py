"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - class information
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
"""

class clsInformation:
    def __init__(self):
        self.QRcodeData = ""    # QRcode data
        self.servoDeg = 0

    def setQRcodeData(self, data):
        self.QRcodeData = data

    def getQRcodeData(self):
        return self.QRcodeData