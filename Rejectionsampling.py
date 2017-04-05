import random
#Rejection sampling for AI Assignment 5
#Made by: Nick Miller
#Help by: Alex Cody, checking to make sure I deined my Bayes Net properly

    #Class containing code for Prior Sampling Methods and rejection sampling function
def priorSample():
    def P(x):
        return (random.random() < x)
    def B():
        #probability for a burglary
        #Will return a boolean
        return P(.02)
    def E():
        #probabilty for an earthquake
        return P(.03)
    def A(b, e):
        #Whether or not the alarm will go off, depending on the burglary and earthquake
        if (b and e):
            return P(.97)
        elif ((b) and not(e)):
            return P(.92)
        elif ((b == False) and e):
            return P(.36)
        elif (not(b) and not(e)):
            return P(.03)
    def J(a):
        #Probability of John calling given the alarm went off
        if (a):
            return P(.85)
        elif (not(a)):
            return P(.07)
    def M(a):
        #Probabilty of Mary calling given the alarm went off
        if (a):
            return P(.69)
        elif (not(a)):
            return P(.02)
    #Calling each function, then putting the results into an array 
    b = B()
    e = E()
    a = A(b,e)
    j = J(a)
    m = M(a)
    #Will return in the form "True, False, True, False, True" in b,e,a,j,m order in the array used in the consistent function
    return [b,e,a,j,m]

def rejection_sampling(query, evidence, trials,Given):
    #Rejection sampling algorithm
    #Query: An array of truth values inputted from the user
    #Evidence: An array of truth values inputted from the user, represent the evidence of a statement
    #trials: The number of tests
    #Given: A boolean value specifying if rejection sampling is testing a statement using conditional probabilty or not
    #If it's not conditonal probabilty, then there is no evidence
    accepted = 0
    matches = 0
    for t in range(trials):
        x = priorSample()
        if (Given == False):
            accepted+= 1
            if consistent(x,query):
                matches += 1
        else:
            if consistent(x,evidence):
                accepted += 1
                if consistent(x, query):
                    matches += 1
    return ((matches*1.0)/accepted)
def consistent(x, evidence):
    ##X: an array of truth values taken from priorSample
    ##evidence: the array being checked, either the query or evidence
    ##Goal: will check to see if these two arrays are equivalent, or consistent
    for i in range(len(x)):
        if (evidence[i] != -1):
            if (evidence[i] != x[i]):
                return False
    return True
def main():
    #Main function to test all the functions above and to run rejeciton sampling
    response = ""
    while (response != "-1"):
        query = []
        evidence = []
        print "Please enter in the form: At Bf Cf"
        print "Or enter in the form: At Bt Cf given Df Et"
        print "Variables are: B - Burglary, E- Earthquake, A - Alarm going off, J - John Calls, M- Mary Calls"
        print "Enter -1 to quit"
        response = raw_input("Please enter the boolean values you wish to test: \n")
        Given = False
        if ("given" in response):
            ##Then, there will be evidence
            container = response.split(" given ")
            query = [-1,-1,-1,-1,-1]
            evidence = [-1,-1,-1,-1,-1]
            queryfromPrompt = container[0].split(" ")
            evidencefromPrompt = container[1].split(" ")
            #Query
            #b,e,a,j,m
            Given = True
            for i in range(len(queryfromPrompt)):
                item = queryfromPrompt[i]
                if ((item == "Bt") or (item == "Bf")):
                    if (item=="Bt"):
                        query[0] = True
                    else:
                        query[0] = False
                if ((item == "Et") or (item == "Ef")):
                    if (item=="Et"):
                        query[1] = True
                    else:
                        query[1] = False
                if ((item == "At") or (item == "Af")):
                    if (item=="At"):
                        query[2] = True
                    else:
                        query[2] = False
                if ((item == "Jt") or (item == "Jf")):
                    if (item=="Jt"):
                        query[3] = True
                    else:
                        query[3] = False
                if ((item == "Mt") or (item == "Mf")):
                    if (item=="Mt"):
                        query[4] = True
                    else:
                        query[4] = False
                        
            for j in range(len(evidencefromPrompt)):
                item = evidencefromPrompt[j]
                if ((item == "Bt") or (item == "Bf")):
                    if (item=="Bt"):
                        evidence[0] = True
                    else:
                        evidence[0] = False
                if ((item == "Et") or (item == "Ef")):
                    if (item=="Et"):
                        evidence[1] = True
                    else:
                        evidence[1] = False
                if ((item == "At") or (item == "Af")):
                    if (item=="At"):
                        evidence[2] = True
                    else:
                        evidence[2] = False
                if ((item == "Jt") or (item == "Jf")):
                    if (item=="Jt"):
                        evidence[3] = True
                    else:
                        evidence[3] = False
                if ((item == "Mt") or (item == "Mf")):
                    if (item=="Mt"):
                        evidence[4] = True
                    else:
                        evidence[4] = False
        else:
            queryfromPrompt = response.split(" ")
            query = [-1,-1,-1,-1,-1]
            evidence = [-1,-1,-1,-1,-1]
            for i in range(len(queryfromPrompt)):
                item = queryfromPrompt[i]
                if ((item == "Bt") or (item == "Bf")):
                    if (item=="Bt"):
                        query[0] = True
                    else:
                        query[0] = False
                if ((item == "Et") or (item == "Ef")):
                    if (item=="Et"):
                        query[1] = True
                    else:
                        query[1] = False
                if ((item == "At") or (item == "Af")):
                    if (item=="At"):
                        query[2] = True
                    else:
                        query[2] = False
                if ((item == "Jt") or (item == "Jf")):
                    if (item=="Jt"):
                        query[3] = True
                    else:
                        query[3] = False
                if ((item == "Mt") or (item == "Mf")):
                    if (item=="Mt"):
                        query[4] = True
                    else:
                        query[4] = False

        print rejection_sampling(query,evidence,10000000, Given)
main()
        
