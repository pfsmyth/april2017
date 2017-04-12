# Part 1 use Pandas to create a new table based on points system

# import the pandas package
import pandas as pd

# read rio medals file 
my_df = pd.read_csv("D:/python_data/Rio_medals_table.csv")

# add a column to a Pandas dataframe
my_df["points"] = my_df.Gold *3 + my_df.Silver *2 + my_df.Bronze


# sort the dataframe by points descending
points_sorted = my_df.sort_values(by=['points'], ascending=False)

# Add a ranking column which represents the new position in the table
# The Rank column has a type of float by default, so we explicitly change it to an int
points_sorted['Rank'] = points_sorted['points'].rank(ascending=False, method='min').astype(int)


# save the data frame as a file
points_sorted.to_csv("D:\\python_data\\Rio_adjusted_table.csv", index=False)


