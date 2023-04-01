import csv

# Initialize variables
total_votes = 0
candidates = []
votes_per_candidate = {}

# Read the CSV file and loop through each row
with open('C:/Users/l1_2p/OneDrive/Desktop/Challenge_3/Starter_Code/PyPoll/Resources/election_data.csv', 'r') as csvfile:
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

# Print results to console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    votes = votes_per_candidate[candidate]
    percentage = votes / total_votes * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > winning_votes:
        winning_candidate = candidate
        winning_votes = votes
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

# Export results to a text file
with open('C:/Users/l1_2p/OneDrive/Desktop/Challenge_3/Starter_Code/PyPoll/election_results.txt', 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        votes = votes_per_candidate[candidate]
        percentage = votes / total_votes * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winning_candidate}\n")
    txtfile.write("-------------------------\n")
