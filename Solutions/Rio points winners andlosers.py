# Part 2 use the Rio_adjusted_table file to decide winners and losers

# function to compare 2 numbers. 
# used to compare the Rank (points based system) with the original pos

def compare(a,b):
    if a > b : return "Winner"
    if a == b : return "No Change"
    if a < b : return "Loser"

# file for output
fw = open(r'D:\python_data\Rio_adjusted_table_winners_losers.csv', 'w')
# input file
fr = open(r'D:\python_data\Rio_adjusted_table.csv', 'r')


hline = fr.readline()                                     
hline = "Win_Lose," + hline    #add new column header as first column
fw.write(hline)                # and write it out  

# for each data line, compare and write output line
for line in fr :
    lb = line.split(',')
    fw.write(compare(int(lb[0]), int(lb[8]))+","+line)
    
fr.close()
fw.close()
