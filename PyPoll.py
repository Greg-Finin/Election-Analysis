# The data we need to retrieve.
# 1. The total number of cotes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each cnadidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable for the file to save and the path. 
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Add the total votes variable.
total_votes = 0

# Create candidate list.
candidate_options = []

# Create vote tracker.
candidate_votes = {}

#Winning candidate  and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the elction results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

     # Read the header row.
    headers = next(file_reader)
    
    #Increment total votes by 1 after each loop.
    for row in file_reader:
        total_votes = total_votes + 1
        
        #Print candidate name from each row.
        candidate_name = row[2]

        #Add candidate name to candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Begin tracking candidate votes.
            candidate_votes[candidate_name] = 0

        #Add vote to candidate
        candidate_votes[candidate_name] += 1

    
    #Calculate vote percentage
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        #Vote percentage
        vote_percentage = (float(votes) / float(total_votes) * 100)
        #Print candidate summary
        print(f'\n {candidate_name}: {votes}: {vote_percentage:.1f}%\n')
        
        #Determine if votes are greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    
# Print winning candidate & stats
print(f'----------------------\n Winner: {winning_candidate}\n Vote Count:{winning_count}\n Vote Percentage: {winning_percentage:.1f} \n ---------------------------')


