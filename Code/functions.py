# functions

# this is a procedure because nothng is returned
def myprocedure(printme) :
    print printme

myprocedure("Hello World")

# this is a function because it returns a value
def xtimesprint(printme, howoften) :
    returnstring = ""
    for x in range(howoften) :
        returnstring = returnstring + printme
    return returnstring

printme = "Hello World "
printme = xtimesprint(printme, 3)
print printme
