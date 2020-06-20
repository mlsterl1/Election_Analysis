# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candiates who recieved votes
# 3. The percenatge of votes each candiate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 
# Assign a variable for the file to load and the path

# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/Election Results.csv")
   
# Create a filename variable to save the file path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and Print the header row. 
    headers = next(file_reader)
    print(headers)
    