import os
import csv
election_data = os.path.join("/Users/sarahwhite/workspace/python_challenge_repo/python-challenge/PyPoll/Resources/election_data.csv")

# A list to store Candidates
candidates = []

# A list to store votes recieved for candidate
num_votes = []

# A list to store the percentage of total votes each candidate recieves
percent_votes = []

# vote counter to tally votes
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote counter 
        total_votes += 1 

        
        # Loop through the values:
        # If the candidate is not on our list, add their name and a vote.
        # If name is already on our list, just add a vote tp the candidate.
        
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    #  Identify winner
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for x in range(len(candidates)):
    print(f"{candidates[x]}: {str(percent_votes[x])} ({str(num_votes[x])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")




# Exporting to .txt file
with open("Election_Results.txt", "w") as new:

    new.write("Election Results")
    new.write("\n")
    new.write("--------------------------")
    new.write("\n")
    new.write(f"Total Votes: {str(total_votes)}")
    new.write("\n")
    new.write("--------------------------")
    new.write("\n")
    for x in range(len(candidates)):
        new.write(f"{candidates[x]}: {str(percent_votes[x])} ({str(num_votes[x])})")
        new.write("\n")
    new.write("--------------------------")
    new.write("\n")
    new.write(f"Winner: {winning_candidate}")
    new.write("\n")
    new.write("--------------------------")