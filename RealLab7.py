# CS1210 Lab7
#
# I certify that the entirety of this file contains only my own work
# and/or that of my assigned partner. I also certify that my partner 
# and I have not shared the contents of this file with anyone in any form.

######################################################################
# Edit the following function definition so it returns a tuple
# strings, where each string represents one of your hawkids.
#
# YOU MUST ENTER BOTH HAWKIDs TO GET CREDIT FOR THIS LAB ASSIGNMENT.
#
# THE AUTOGRADER WILL FAIL TO ASSIGN A GRADE IF YOUR HAWKIDs ARE
# NOT PROPERLY INCLUDED IN THIS FUNCTION. CAVEAT EMPTOR.
######################################################################
def hawkid():
    return(("jtkolich", "kscales"))

######################################################################
# power(B, N) returns B^N, that is, B raised to the Nth power. Your
# solution must be recursive, where the base case corresponds to B==0
# and the recursive step makes progress towards this base case by
# reducing B in the recursive call. Note: You can assume N>0 and B>=0.
def power(B, N):
    if N == 0:
        return(1)
    return (B*power(B,N-1))

######################################################################
# addEmUp(N) takes a (possibly multi-digit) integer, N, and returns a
# single digit integer obtained by the individual digits of N
# repeatedly until only one digit remains. Note: You can assume N>0.
def addEmUp(N):
    if N<10:
        return(N)
    p = 0
    for i in str(N):
        p = p+int(i)
    return(addEmUp(p))
        
######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid() == ("hawkid1", "hawkid2"):
    print('### Error: for heavens sake ENTER YOUR HAWKIDs in the hawkid() function!')
    print('### The Autograder will assign this submission 0 points.')
