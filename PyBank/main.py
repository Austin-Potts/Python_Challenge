#importing os module that allows us to work with file systems
import os 
#importing csv which allows us to read csv files
import csv
#had to import pathlib to export text file
from pathlib import Path 

#relative path to read in the csv later
budget_csv = os.path.join('Desktop','python-challenge','PyBank','Resources','budget_data.csv')
#create empty lists which will be appended later
totalMonths = []
netProfit = []
monthlyChange = []
 
# Open csv and read in line by line
with open(budget_csv,newline="", encoding="utf-8") as budget:

     # Store the data of the budget csv into csvreader
    csvreader = csv.reader(budget,delimiter=",") 

    # Skip the header 
    header = next(csvreader)  

    # Iterate through the rows in the csv
    for row in csvreader: 

        # Append the total months and total profit lists
        totalMonths.append(row[0])
        netProfit.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(netProfit)-1):
        
        # Take the difference between two months and append to monthly change
        monthlyChange.append(netProfit[i+1]-netProfit[i])
        
# Obtain the max and min of the the montly profit change list
maxIncrease = max(monthlyChange)
maxDecrease = min(monthlyChange)

# Correlate max and min to the proper month using month list and index from max and min
#Plus 1 at the end to associate with the next month
bestMonth = monthlyChange.index(max(monthlyChange)) + 1
worstMonth = monthlyChange.index(min(monthlyChange)) + 1 

# Print financial analysis

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(totalMonths)}")
print(f"Total: ${sum(netProfit)}")
print(f"Average Change: {round(sum(monthlyChange)/len(monthlyChange),2)}")
print(f"Greatest Increase in Profits: {totalMonths[bestMonth]} (${(str(maxIncrease))})")
print(f"Greatest Decrease in Profits: {totalMonths[worstMonth]} (${(str(maxDecrease))})")

#creating the output file path which will have a text document added to it
output_file = Path('Desktop','python-challenge','PyBank','Resources','Financial_Analysis_Summary.txt')

with open(output_file,"w") as file:
    
# Write Financial_Analysis_Summary text document
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(totalMonths)}")
    file.write("\n")
    file.write(f"Total: ${sum(netProfit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthlyChange)/len(monthlyChange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {totalMonths[bestMonth]} (${(str(maxIncrease))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {totalMonths[worstMonth]} (${(str(maxDecrease))})")