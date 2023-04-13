import csv
import os

# Set input file path
input_file = os.path.join("Resources", "election_data.csv")

# Set output file path
output_file = os.path.join("Analysis_output", "election_results.txt")

# Initialize variables
total_votes = 0
candidates = []
votes_per_candidate = {}

# Read the CSV file and loop through each row
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row
    for row in csvreader:
        # Increment the total number of votes
        total_votes += 1
        
        # Check if the candidate has already been added to the list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1

# Initialize variables for calculating the winner
winning_candidate = ""
winning_votes = 0

# Format results
output = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------"""
for candidate in candidates:
    votes = votes_per_candidate[candidate]
    percentage = votes / total_votes * 100
    output += f"\n{candidate}: {percentage:.3f}% ({votes})"
    if votes > winning_votes:
        winning_candidate = candidate
        winning_votes = votes
output += f"\n-------------------------\nWinner: {winning_candidate}\n-------------------------"

# Print results to console
print(output)

# Export results to a text file
with open(output_file, 'w') as txtfile:
    txtfile.write(output)


