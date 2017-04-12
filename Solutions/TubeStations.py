f = open(r'd:\python_data\tubestations.csv', 'r') #prefix the file path with 'r' to stop the '\' being treated as escape characters
## Read the first line  and ignore
name = f.readline()

for name in f :
    count = 0
    lc_name = name.lower().strip()              # convert to lowercase and remove the newline character ("\n")
    for x in ['a', 'e', 'i', 'o', 'u']:         # check for each vowel in turn
        if x in lc_name:
            count = count +1                    # if vowel is present add one to count  
    if count == 5: print lc_name                # only if count has reached five do I print 
    
    
f.close()
