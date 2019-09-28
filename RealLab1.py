# CS1210 Lab1
# Section A01
# I certify that the entirety of this file contains only my own work
# and/or that of my assigned partner. I also certify that my partner 
# and I have not shared the contents of this file with anyone in any form.

######################################################################
# Edit the following function definition, replacing the words
# 'hawkid1' and 'hawkid2' with your respective hawkids.
#
# Note: Your hawkid is the login name you use to access ICON.
#
# YOU MUST ENTER BOTH HAWKIDs TO GET CREDIT FOR THIS LAB ASSIGNMENT.
#
# For example, if my assigned partner were Joe Schroeder with hawkid
# "jschroeder", the correct hawkid() function would now read:
#
# def hawkid():
#     return(("jschroeder", "segre"))
#
# Note the quotation marks around each identifier and the exact
# parenthisization and punctuation used.
#
# THE AUTOGRADER WILL FAIL TO ASSIGN A GRADE IF YOUR HAWKIDs ARE
# NOT PROPERLY INCLUDED IN THIS FUNCTION. CAVEAT EMPTOR.
#
# If you are a three-person group, change the second line
# of the function template to read:
#   return(("hawkid1", "hawkid2", "hawkid3"))
# and then edit as appropriate.
######################################################################
def hawkid():
    return(("Jtkolich", "javega"))

######################################################################
# Convert meters (m) to feet (f): 1 m = 3.28084 ft.
def m2ft (value):
    feet = value *3.28084
    return(feet)

# Convert meters (m) to feet (f): 1 m = 3.28084 ft. 
def ft2m (value):
    meters = value /3.28084
    return(meters)

######################################################################
# Convert knots (kn) to kilometers per hour (kph): 1 kn = 1.852001 kph.
def kn2kph (value):
    kph = value*1.852001
    return(kph)

# Convert kilometers per hour (kph) to knots (kn): 1 kn = 1.852001 kph.
def kph2kn (value):
    kn=value/1.852001
    return(kn)

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid() == ("hawkid1", "hawkid2"):
    print('### Error: for credit, you MUST provide your hawkid in the hawkid() function.')
    print('### The Autograder will assign this submission 0 points.')
