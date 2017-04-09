#command line arguments
import sys

print "first parameter is ", sys.argv[1]
print "second parameter is ", sys.argv[2]
print "the program name is ", sys.argv[0]

print len(sys.argv)
for arg in sys.argv: 
    print arg
    
