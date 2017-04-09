# string.split()

mystring = "5,GER,17,10,15,42,View medals by sport for Germany"

mylistofitems = mystring.split(",")

print "\n the list created by the split\n"
print(mylistofitems)

print "\n an individual item with index 1\n"
print(mylistofitems[1])

print "\n all of the list items seperately\n"
for item in mylistofitems :
    print(item)

print "\n the types of all of the list items seperately\n"
for item in mylistofitems :
    print(type(item))


# string.lower
print "\n example of the lower() function\n"
print mystring.lower()

# string.join
print "\n example of the join() function\n"
print ','.join(mylistofitems)
