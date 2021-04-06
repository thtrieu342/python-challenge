import os
import csv

csvfile = os.path.join("Resources", "election_data.csv")

with open (csvfile, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #skip header row
    csvheader = next(csvreader)
    #print(csvheader)

    #defining variables
    total_votes = 0
    candidates = []
    candidate_vote = {}
    win_count = 0
    winner = ""
    
    #calculating total_votes
    for row in csvreader:
        
        total_votes = total_votes + 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_vote[candidate] = 0
        candidate_vote[candidate]=candidate_vote[candidate] + 1

print("Election Results:")
print("-------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------")

#calculating the winner
for candidate in candidate_vote:
    vote = candidate_vote.get(candidate)
    percentage_vote = float(vote)/float(total_votes) * 100
        
    if (vote > win_count):
        win_count = vote
        winner = candidate
    vote_result = f"{candidate}: {percentage_vote:.2f}% ({vote})\n"
    print(vote_result, end = "")

print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")

#exporting text file
output_file = os.path.join("Analysis", "Analysis.txt")
with open (output_file, 'w') as text_file:
    text_file.write("Election Results:")
    text_file.write("\n-------------------------------")
    text_file.write(f"\nTotal Votes: {total_votes}")
    text_file.write("\n-------------------------------")
    text_file.write(f"\n{vote_result}")
    text_file.write("\n-------------------------------")
    text_file.write(f"\nWinner: {winner}")
    text_file.write("\n-------------------------------")
    
