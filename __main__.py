"""
File: __main__.py

Project: Vcard to QR Code Generator

Description: Encode a user's personal information into a QR code
             that expands to a full-fledged Vcard file when scanned.

Programmer: Amy Ariel

"""

"""
Future Notes:
    Add website field
    Add social mediae
    Add state machine to determine what data members have been set / added to card
"""

import qrvcard_infoclass
import qrvcard_functions

# establish objects to receive user info
userName = qrvcard_infoclass.name()
userPersonal = qrvcard_infoclass.contact()
userWork = qrvcard_infoclass.contact()

# get all info

userName.setfirstName(str(input("First name? ")))
userName.setlastName(str(input("Last name? ")))

while(True):
    print("Add information:")
    print("\t(a) Review current information and Continue")
    print("\t(b) Replace name")
    print("\t(c) Add/replace job title/company")
    print("\t(d) Add/replace personal phone")
    print("\t(e) Add/replace work phone")
    print("\t(f) Add/replace personal email")
    print("\t(g) Add/replace work email")
    print("\t(h) Add/replace personal address")
    print("\t(i) Add/replace work address")
    print()

    choice = input("\t\tChoice? ")

    if choice == 'a':
        qrvcard_functions.echo(userName, userPersonal, userWork)
        if (input("\n Correct? Y/N ") == "Y"):
            break
    elif choice == 'b':
        userName.setfirstName(str(input("First name? ")))
        userName.setlastName(str(input("Last name? ")))
    elif choice == 'c':
        userName.setjobTitle(str(input("Job title? ")))
        userName.setcompany(str(input("Company? ")))
    elif choice == 'd':
        userPersonal.setphone(str(input("Mobile phone? ")))
    elif choice == 'e':
        userWork.setphone(str(input("Work phone? ")))
    elif choice == 'f':
        userPersonal.setemail(str(input("Personal email? ")))
    elif choice == 'g':
        userWork.setemail(str(input("Work email? ")))
    elif choice == 'h':
        userPersonal.setstreet(str(input("Peronsal address - street? ")))
        userPersonal.setcity(str(input("Personal address - city? ")))
        userPersonal.setstate(str(input("Personal address - state? ")))
        userPersonal.setzip(str(input("Personal address - zip code? ")))
    elif choice == 'i':
        userWork.setstreet(str(input("Work address - street? ")))
        userWork.setcity(str(input("Work address - city? ")))
        userWork.setstate(str(input("Work address - state? ")))
        userWork.setzip(str(input("Work address - zip code? ")))
    else:
        print("\t\tEnter option a-h")