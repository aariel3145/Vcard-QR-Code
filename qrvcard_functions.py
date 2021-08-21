"""
File: qrvcard_functions.py

Project: Vcard to QR Code Generator

Description: Encode a user's personal information into a QR code
             that expands to a full-fledged Vcard file when scanned.

Programmer: Amy Ariel

"""

def echo(userName, userPersonal, userWork):
    print(userName.getfirstName(), userName.getlastName())
    print(f"{userName.getjobTitle()} at {userName.getcompany()}")
    print(f"Mobile: {userPersonal.getphone()} / Work: {userWork.getphone()}")
    print(f"Personal: {userPersonal.getemail()} / Work: {userWork.getemail()}")
    print("Home: ")
    print(userPersonal.getstreet())
    print(f"{userPersonal.getcity()}, {userPersonal.getstate()} {userPersonal.getzip()}")
    print("Work: ")
    print(userWork.getstreet())
    print(f"{userWork.getcity()}, {userWork.getstate()} {userWork.getzip()}")
    print("Website: ")
    print(userSocial.getwebsite())
    print(f"Facebook: {userSocial.getfacebook} / LinkedIn: {userSocial.getlinkedin} / Instagram: @{userSocial.getinstagram}")
