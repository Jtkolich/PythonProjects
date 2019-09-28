# CS1210 Lab6
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
    return(("jtkolich", "srbnsn"))

######################################################################
# flip(L) takes a list, L and modifies it to reverse the order of its
# corresponding elements. The function should not return a value; its
# effect can be observed by comparing L before and after invocation.
#
# >>> L = [1, 2, 3, 4]
# >>> flip(L)
# >>> L
# [4, 3, 2, 1]
#
# For credit, your solution should directly manipulate L; you are not
# allowed to use L.reverse() to flip the list.
#
def flip(L):
    for n in range((len(L)//2)):
        L[n],L[-1-n] = L[-1-n],L[n]
    return (L)

######################################################################
# invert(L) that takes a list, L, and returns a dictionary whose keys
# are the elements of L and the corresponding values are the index of
# the first occurrance of the element in L.
#
# >>> L = [0, 1, 2, 0, 4]
# >>> invert(L)
# {4: 4, 0: 0, 2: 2, 1: 1}
#
# For full credit, your function should (i) associate the first
# location found for each duplicated value in L (n.b., value 0 is
# found in locations 0 and 3, but 0:0 and not 0:3 appears in the
# example above), and (ii) run in O(N) time (n.b., beware of using
# list methods that are themselves O(N)).
#
def invert(L):
    return{x:L.index(x) for x in L}

######################################################################
# vowelIndex(S), that returns a dictionary whose keys are the words in
# S and the corresponding values are the number of vowels (a, e, i, o
# or u) in that word.
#
# >>> vowelIndex("The rain in Spain falls mainly in the plains")
# {'The': 1, 'rain': 2, 'in': 1, 'Spain': 2, 'falls': 1, 'mainly': 2, 'the': 1, 'plains': 2}
# >>> vowelIndex("Four score and seven years ago")
# {'Four': 2, 'score': 2, 'and': 1, 'seven': 2, 'years': 2, 'ago': 2}
#
# Note that each individual word's case is unchanged in the keys of
# the dictionary returned.
#
def vowelIndex(S):
    return{V:len(['aeiou' in V]) for V in S.split()}
