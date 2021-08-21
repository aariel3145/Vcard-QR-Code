"""
File: qrvcard_infoclass.py

Project: Vcard to QR Code Generator

Description: Encode a user's personal information into a QR code
             that expands to a full-fledged Vcard file when scanned.

Programmer: Amy Ariel

"""

class name:
    """
    Class with user's personal information
        - first/last name
        - job title
        - company
    """

    def __init__(self):
        """
        Summary: Constructor function for info object
        Parameters: none, except self
        Returns: nothing
        """

        self.firstName = '[FIRST NAME]'
        self.lastName = '[LAST NAME]'
        self.jobTitle = '[JOB TITLE]'
        self.company = '[COMPANY]'

    ###
    # class setters
    ###

    def setfirstName(self, fname):
        """
         Summary: sets firstName in object as variable fname
         Parameters: fname - variable that holds object's first name
         Return: none
        """

        self.firstName = fname

    def setlastName(self, lname):
        """
         Summary: sets lastName in object as variable lname
         Parameters: lname - variable that holds object's last name
         Return: none
        """

        self.lastName = lname

    def setjobTitle(self, jtitle):
        """
         Summary: sets jobTitle in object as variable jtitle
         Parameters: jtitle - variable that holds object's job title
         Return: none
        """

        self.jobTitle = jtitle

    def setcompany(self, co):
        """
         Summary: sets company in object as variable co
         Parameters: co - variable that holds object's company
         Return: none
        """

        self.company = co

    ###
    # class getters
    ###
    def getfirstName(self):
        """
         Summary: gets object's first name
         Parameters: none, other than self
         Return: variable type string of first name
        """

        return self.firstName

    def getlastName(self):
        """
         Summary: gets object's last name
         Parameters: none, other than self
         Return: variable type string of last name
        """

        return self.lastName

    def getjobTitle(self):
        """
         Summary: gets object's job title
         Parameters: none, other than self
         Return: variable type string of job title
        """

        return self.jobTitle

    def getcompany(self):
        """
         Summary: gets object's company
         Parameters: none, other than self
         Return: variable type string of company
        """

        return self.company

# end name class

class contact:
    """
    Summary: Class with user's contact info
        - phone
        - email
        - address (street, city, state, zip)
    """

    def __init__(self):
        """
         Summary: constructor function for contact object
         Parameters: none, other than self
         Return: nothing
        """
    
        self.phone = '[PHONE]'
        self.email = '[EMAIL]'
        self.street = '[STREET]'
        self.city = '[CITY]'
        self.state = '[STATE]'
        self.zip = '[ZIP]'

    def setphone(self, ph):
        """
         Summary: sets phone in object as variable ph
         Parameters: ph - variable that holds object's phone number
         Return: none
        """
    
        self.phone = ph
    
    def setemail(self, eml):
        """
         Summary: sets email in object as variable eml
         Parameters: eml - variable that holds object's email address
         Return: none
        """
    
        self.email = eml
    
    def setstreet(self, strt):
        """
         Summary: sets street in object as variable strt
         Parameters: strt - variable that holds object's street
         Return: none
        """
    
        self.street = strt
    
    def setcity(self, cty):
        """
         Summary: sets city in object as variable cty
         Parameters: cty - variable that holds object's city
         Return: none
        """
    
        self.city = cty
    
    def setstate(self, st):
        """
         Summary: sets state in object as variable st
         Parameters: st - variable that holds object's state
         Return: none
        """
    
        self.state = st
    
    def setzip(self, zp):
        """
         Summary: sets zip in object as variable zp
         Parameters: zp - variable that holds object's zip code
         Return: none
        """
    
        self.zip = zp
    
    def getphone(self):
        """
         Summary: gets object's phone
         Parameters: none, other than self
         Return: variable type string of phone
        """
    
        return self.phone
    
    def getemail(self):
        """
         Summary: gets object's email
         Parameters: none, other than self
         Return: variable type string of email
        """
    
        return self.email
    
    def getstreet(self):
        """
         Summary: gets object's street
         Parameters: none, other than self
         Return: variable type string of street
        """
    
        return self.street
    
    def getcity(self):
        """
         Summary: gets object's city
         Parameters: none, other than self
         Return: variable type string of city
        """
    
        return self.city
    
    def getstate(self):
        """
         Summary: gets object's state
         Parameters: none, other than self
         Return: variable type string of state
        """
    
        return self.state
    
    def getzip(self):
        """
         Summary: gets object's zip
         Parameters: none, other than self
         Return: variable type string of zip
        """
    
        return self.zip
# end contact class

class social:
    """
    Summary: Class with user's social media
        - website
        - Facebook
        - LinkedIn
        - Instagram
    """

    def __init__(self):
        """
         Summary: constructor function for social object
         Parameters: none, other than self
         Return: nothing
        """
    
        self.website = '[WEBSITE]'
        self.facebook = '[FACEBOOK]'
        self.linkedin = '[LINKEDIN]'
        self.instagramm = '[INSTAGRAM]'

    def setwebsite(self, site):
        """
            Summary: sets website in object as variable site
            Parameters: site - variable that holds object's website
            Return: none
        """

            self.website = site
    
    def setfacebook(self, fb):
        """
            Summary: sets facebook in object as variable fb
            Parameters: fb - variable that holds object's facebook
            Return: none
        """

            self.facebook = fb

    def setlinkedin(self, li):
        """
            Summary: sets linkedin in object as variable li
            Parameters: li - variable that holds object's linkedin
            Return: none
        """

            self.linkedin = li

    def setinstagram(self, insta):
        """
            Summary: sets instagramm in object as variable insta
            Parameters: insta - variable that holds object's instagram
            Return: none
        """

            self.instagram = insta

    def getwebsite(self):
        """
        Summary: gets object's website
        Parameters: none, other than self
        Return: variable type string of wesite
        """
    
        return self.website

    def getfacebook(self):
        """
        Summary: gets object's facebook
        Parameters: none, other than self
        Return: variable type string of facebook
        """
    
        return self.facebook

    def getlinkedin(self):
        """
        Summary: gets object's linkedin
        Parameters: none, other than self
        Return: variable type string of linkedin
        """
    
        return self.linkedin

    def getinstagram(self):
        """
        Summary: gets object's instagram
        Parameters: none, other than self
        Return: variable type string of instagram
        """
    
        return self.instagram

# end social class
