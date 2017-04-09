#
#The three line below are the contents of the Hellworld.py file
#
#def psHW(who):
#    ''' This is the help comment. '''
#    print "Hello World to", who




# import a specific function
# assuming the name is unique, I can use it like any other built-in function

from Helloworld import psHW
help(psHW)
psHW("Peter")

# import all of the functions in the module (file)
# specify an alias and then prefix the calls to the function with the alias

import Helloworld  as ps
help(ps.psHW)
ps.psHW("Peter")
