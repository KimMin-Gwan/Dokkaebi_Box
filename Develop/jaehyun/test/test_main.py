"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - test Main
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
"""
from dokkaebi_Raspberry import *

def main():
    dokkaebi_RaspberryPI = dokkaebi_Raspberry()
    while True:
        dokkaebi_RaspberryPI.dokkaebi_Rasp_Magnetic.getMagneticDoorState()


if __name__ == "__main__":
    main()
