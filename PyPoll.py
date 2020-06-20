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


#Initialize a total vote counter
total_votes = 0 

# Candidate Options and candidate votes
candidate_options = []

# 1. Declare the empty dictionary. 
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
    
    # Print each row in the csv file. 
    for row in file_reader:
        # Add to the total vote count. 
        total_votes += 1 

       # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options: 
           candidate_options.append(candidate_name)

           # Begin tracking that candidate's vote count. 
           candidate_votes[candidate_name] = 0

        # Add a vote to that canidate's count. 
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print the candidate name, vote count and percentage of votes to the terminal

    # Determine winning vote count and candiate
    # Determine if the votes is greater than the winning count. 
    if (votes > winning_count) and (vote_percentage > winning_percentage):
       # If true then set winning_count = votes and winning_percent = vote percentages
       winning_count = votes
       winning_percentage = vote_percentage
       # And, set the winning_candidate equal to the candidate's name.
       winning_candidate = candidate

#  To do: print out the winning candidate, vote count and percentage to terminal
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



