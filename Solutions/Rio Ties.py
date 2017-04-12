# Finding out which countries tied
tieList = []                                            # list to store the tied countries
tieflag = False                                         # initially there are no ties
Position = 0                                            # variables for storing what else I need to print 
Gold = 0
Silver = 0
Bronze = 0


fr = open(r'D:\python_data\Rio_medals_table.csv', 'r')
hline = fr.readline()                                   # header line - ignore this

fline = fr.readline()                                   # read and split first data line for comparison with next
la = fline.split(',')

for line in fr :                                        # iterate through the rest of the file
    lb = line.split(',')
    if lb[2] == la[2] and lb[3] == la[3] and lb[4] == la[4] :  # we have a tie, index[2,3 and 4] are Gold, Silver and Bronze medals
        if tieflag :
            tielist.append(lb[1])                              # add the new tied country to the current tied list
        else :                                                 
            tielist = []                                       # new tie, so reset the tielist and 
            tielist.append(la[1])                              # add both to the new list 
            tielist.append(lb[1])
            tieflag = True
            Position = lb[0]
            Gold = lb[2]
            Silver = lb[3]
            Bronze = lb[4]
    else :                                                     # not a tie or end of a tie
        if tieflag :
            print','.join(tielist),'Tied in position', Position,  'with', str(Gold), 'Golds,', str(Silver), 'Silver and', str(Bronze), 'Bronze medals'
            tieflag = False
    la = lb
if tieflag :                                                   # check for tie at end of file
    print ','.join(tielist),'Tied in position', Position,  'with', str(Gold), 'Golds,', str(Silver), 'Silver and', str(Bronze), 'Bronze medals'   
fr.close()
