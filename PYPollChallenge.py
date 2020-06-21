# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/Election Results.csv")
   
# Create a filename variable to save the file path
file_to_save = os.path.join("analysis", "election_analysis_challenge.txt")

#Initialize a total vote counter
total_votes_county = 0 

# County Options and county votes
county_options = []

# 1. Declare the empty dictionary. 
county_votes = {}

# Winning County and Winning Count Tracker
winning_county = ""
winning_count_county = 0
winning_percentage_county = 0

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)

 # Print each row in the csv file. 
    for row in file_reader:
     # Add to the total vote count. 
        total_votes_county += 1 

     # Print the county name from each row.
        county_name = row[1]

        # Add the county_name to the county list.
        if county_name not in county_options: 
            county_options.append(county_name)

            # Begin tracking the county vote count. 
            county_votes[county_name] = 0

        # Add a vote to that county's count. 
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes_county:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    for county in county_votes:
        # Retrieve county vote count and percentage.
        votes_counties = county_votes[county]
        vote_percentage_county = float(votes_counties) / float(total_votes_county)*100
        county_results = (f"{county}: {vote_percentage_county:.1f}% ({votes_counties:,})\n")

        # Print each county voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and winning county.
        if (votes_counties > winning_count_county) and (vote_percentage_county > winning_percentage_county):
            winning_count_county = votes_counties
            winning_county = county
            winning_percentage_county = vote_percentage_county
    # Print the winning county results to the terminal.
    largest_county_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(largest_county_turnout)
    # Save the winning candidate's results to the text file.
    txt_file.write(largest_county_turnout)

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
# Save the results to our text file.
with open(file_to_save, "a") as txt_file:
    
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
