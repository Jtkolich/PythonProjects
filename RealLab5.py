# CS1210 Lab5
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
    return(("jtkolich"))

######################################################################
# readGrades(F) takes a filename, F, opens it, and reads in the
# contents of the comma-separated file F. The file consists of a
# header line (labeling each column) followed by some number of lines
# containing two values, a student identified and a grade. After
# printing an informative message of the form "Read 100 values.",
# readGrades(F) should returns a dictionary consisting of SID:grade
# pairs. So if F looks like:
#   SID,grade
#   0415,42
#   0003,10
#   0220,91
#   0324,39
#   0178,8
#   0346,23
#   0192,22
#   0332,25
# followed by some additional lines, your solution should print:
#   Read 100 values.
# and then return a value that looks something like:
#   { "0415":42, "0178":8, "0332":25, "0003":10 ...}
# although the order is not guaranteed.
#
def readGrades(F):
    infile = open('filename',r)
    s = infine.read()
    return{"SID":grade}
    
######################################################################
# computeRank(D) should modify dictionary D (e.g., dictionary returned
# by readGrades()) so that the value is a tuple (grade, rank). No
# value is returned. Rank is 1-indexed, where the highest grade gets
# rank 1 and the lowest grade gets rank N, where N is the number of
# entries in the dictionary. Ties should be assigned the same rank.
#
def computeRank(D):
    pass

######################################################################
# writeGrades(D, F) should write a header reading "SID,grade,rank" to
# the file named F followed by a comma-separated line corresponding to
# each entry in D, in sorted order by SID. The contents of the file
# should read, e.g.:
#    SID,Grade,Rank
#    0003,10,86
#    0024,57,39
#    0038,39,57
#    0045,82,17
#    0049,74,20
# followed by the remaining lines (note sorted order).
#
def writeGrades(D, F):
    pass
