import os
import csv
election_data = os.path.join("/Users/sarahwhite/workspace/python_challenge_repo/python-challenge/PyPoll/Resources/election_data.csv")

# list to store the Candidates
candidates = []

# list to store votes recieved for each candidate
candidate_votes = []

# list to store the percentage of total votes each candidate gets
percent_votes = []

# vote counter to tally votes
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
    # add votes to the counter 
        total_votes += 1 

        
    # Loop through the values:
    # If the candidate is not on the list, add  name and a vote.
    # If name is on list, just add a vote for that candidate.
        
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1
    
# Add to percent_votes list 
    for votes in candidate_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
#  Identify the  winner
    winner = max(candidate_votes)
    index = candidate_votes.index(winner)
    winning_candidate = candidates[index]

# print final results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for x in range(len(candidates)):
    print(f"{candidates[x]}: {str(percent_votes[x])} ({str(candidate_votes[x])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")




# Export results to .txt file
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
        new.write(f"{candidates[x]}: {str(percent_votes[x])} ({str(candidate_votes[x])})")
        new.write("\n")
    new.write("--------------------------")
    new.write("\n")
    new.write(f"Winner: {winning_candidate}")
    new.write("\n")
    new.write("--------------------------")