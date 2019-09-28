# CS1210 Lab8
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
    return(('jtkolich', "hawkid2"))

######################################################################
# Transcript() class from Exam 2. The three variables G, id and T are
# established at instance creation: self.G contains a fixed conversion
# table (from letter grades to grade points); self.id is the student
# id number, and self.T is a dictionary containing the student's
# transcript which is read in from the filename specified at creation.
class Transcript():
    def __init__(self, id, filename):
        self.G = {'A+':4.33, 'A':4, 'A-':3.67, 'B+':3.33, 'B':3, 'B-':2.67, 'C+':2.33, 'C':2, 'C-':1.67, 'D+':1.33, 'D':1, 'D-':0.67, 'F':0}
        self.id = int(id)
        self.T = {}
        self.readFile(filename)
        
    # Provides a nice printed representation when the object is evaluated.
    def __repr__(self):
        S = "Student {}\n".format(self.id)
        for term in self.terms():
            S = S + "  Term {}: {} sch => {}\n".format(term, str(self.termHours(term)), str(self.termGPA(term)))
        S = S + "Cumulative GPA: {}".format(str(self.cumGPA()))
        return(S)
            
    # Reads in grades from specified filename at instance creation.
    def readFile(self, filename):
        file = open(filename, 'r')
        for line in file:
            # Each record in file is "term,class,sch,grade"
            record = line.strip().split(',')
            # If the term already has an entry in T, append the new
            # record, else create the key/value pair with this term aas
            # key and the current record as its only value.
            if record[0] in self.T:
                self.T[record[0]].append((record[1], int(record[2]), record[3]))
            else:
                self.T[record[0]] = [(record[1], int(record[2]), record[3])]
        # Clean up after yourself.
        file.close()

    # Access functions returns list of terms in sorted order.
    def terms(self):
        return(sorted(self.T.keys()))

    # Returns number of credit hours for specified term.
    def termHours(self, term):
        return(sum([int(i[1]) for i in self.T[term]]))

    # Returns number of grade points earned in specified term.
    def termPoints(self, term):
       x = [j[2] for j in self.T[term]]
       for k in range(len(x)):
           x[k] = self.G[x[k]]
        y = [a[1] for a in range(len(x))
             

    # Computes and returns the GPA for the specified term.
    def termGPA(self, term):
        pass

    # Computes and returns the cumulative GPA. Note that this
    # is not the same as the average term GPA; you need to
    # weight the cumulative GPA by credit hours earned.
    def cumGPA(self):
        x = sum(self.termPoints(term) for term in self.T)
        return (x / sum(self.termHours(term) for term in self.T))
             

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid() == ("hawkid1", "hawkid2"):
    print("### Error: for heaven's sake ENTER YOUR HAWKIDs in the hawkid() function!")
    print('### The Autograder will assign this submission 0 points.')
