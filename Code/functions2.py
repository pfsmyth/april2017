def xtimesprint(printme, howoften = 1) :
    '''
    This function repeats the string provided in the printme parameter
    the number of times specified in the howoften parameter.
    The howoften parameter has a default value of 1
    '''
    returnstring = ""
    for x in range(howoften) :
        returnstring = returnstring + printme 
    return returnstring

printme = "Hello World"
printme = xtimesprint(printme, 3)
print(printme)
help(xtimesprint)
