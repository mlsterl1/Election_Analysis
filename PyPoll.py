# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candiates who recieved votes
# 3. The percenatge of votes each candiate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 
# Assign a variable for the file to load and the path

file_to_load = 'Election Results.csv'
# Open the election results and read the file. 
election_data = open(file_to_load, 'r')
# to do : perform analysis 
# close the file. 
election_data.close()


