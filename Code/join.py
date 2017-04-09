# string.join()

mystring = "5,GER,17,10,15,42,View medals by sport for Germany"
print "The original string\n", mystring

print "\n The individual list items after the split\n"
mylistofitems = mystring.split(",")
for item in mylistofitems :
    print item
    
print "\nThe string after the join\n"
my_joined_string = ','.join(mylistofitems)
print my_joined_string
