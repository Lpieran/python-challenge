import csv
import os

# Set file paths
csv_file_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("Analysis", "budget_analysis.txt")

# Initialize variables
total_months = 0
total_profit = 0
previous_profit = 0
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999999]

# Read data from csv file
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        # Count total months
        total_months += 1

        # Calculate total profit
        current_profit = int(row[1])
        total_profit += current_profit

        # Calculate profit change
        if total_months == 1:
            previous_profit = current_profit
        else:
            profit_change = current_profit - previous_profit
            profit_change_list.append(profit_change)
            previous_profit = current_profit

            # Find greatest increase and decrease in profit
            if profit_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_change

            if profit_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_change

# Calculate average profit change
average_change = sum(profit_change_list) / len(profit_change_list)

# Format results
output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit}
Average Change: ${round(average_change, 2)}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"""

# Print results to console
print(output)

# Write results to a text file
with open(output_path, "w") as output_file:
    output_file.write(output)
