# CS1210 Lab4
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
    return(("cwhughes", "jtkolich"))

######################################################################
# Given a string, S, consisting of one or more ``words'' (i.e.,
# substrings separated by spaces), return a list of integers denoting
# the lengths of these word substrings.
#
# >>> wordLengths("The rain in Spain falls mainly in the plains.")
# [3, 4, 2, 5, 5, 6, 2, 3, 7]
# >>> wordLengths("Deoxyribonucleicacid")
# [20]
def wordLengths(S):
    return([len(w) for w in S.split()])

######################################################################
# Given an integer, max, and a list of integers, L, where each element
# of L is <= max, return a list containing all integers 0 < i < max
# such that i is divisible by at least one element of L.
#
# >>> collect(15, [3, 4])
# [3, 4, 6, 8, 9, 12]
# >>> collect(100, [7, 11, 13])
# [7, 11, 13, 14, 21, 22, 26, 28, 33, 35, 39, 42, 44, 49, 52, 55, 56, 63, 65, 66, 70, 77, 78, 84, 88, 91, 98, 99]
def collect(max, L):
    return([i for i in range(1,max) for j in range(len(L)) if i%L[j]==0] )

######################################################################
# Given a string, S, return a dictionary containing entries of the
# form v:N where v is one of 'aeiou' and N is the number of
# occurrances of v in S. Note: the dictionary returned should only
# return non-zero entries.
#
# >>> vowelCount("The rain in Spain falls mainly in the plains")
# {'a': 5, 'e': 2, 'i': 6}
# >>> vowelCount("Deoxyribonucleicacid")
# {'a': 1, 'e': 2, 'i': 3, 'o': 2, 'u': 1}
def vowelCount(S):
    return ({v.lower():S.lower().count(v) for v in S.lower() if v.lower() in 'aeiou'})

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid() == ("hawkid1", "hawkid2"):
    print('### Error: for credit, you MUST provide your hawkids in the hawkid() function.')
    print('### The Autograder will assign this submission 0 points.')
