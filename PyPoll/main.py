#importing os module that allows us to work with file systems
import os 
#importing csv which allows us to read csv files
import csv

from pathlib import Path 


election_csv = os.path.join('Desktop','python-challenge','PyPoll','Resources','election_data.csv')

# Declare Variables 
totalVotes = 0 
khanVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0

#open the csv file anf read it line by line
with open(election_csv,newline="", encoding="utf-8") as poll:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(poll,delimiter=",") 

    # Skip the header labels to iterate with the values
    header = next(csvreader)  

    # Iterate through the rows in the election data csv
    for row in csvreader: 
         # Count the unique Voter ID's and store in variable  called totalVotes
        totalVotes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Khan": 
            khanVotes +=1
        elif row[2] == "Correy":
            correyVotes +=1
        elif row[2] == "Li": 
            liVotes +=1
        elif row[2] == "O'Tooley":
            otooleyVotes +=1

 # Create two lists out of the data which will be used to find the winner
candidates = ["Khan", "Correy", "Li","O'Tooley"]
voteCounts = [khanVotes, correyVotes,liVotes,otooleyVotes]

# Zip together the lists candidate(key) and voteCounts(value) into a dictionary
# Find the winner by using the max function on the dictionary
dict_candidates_and_votes = dict(zip(candidates,voteCounts))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis in % terms
khan_percent = (khanVotes/totalVotes) *100
correy_percent = (correyVotes/totalVotes) * 100
li_percent = (liVotes/totalVotes)* 100
otooley_percent = (otooleyVotes/totalVotes) * 100

# Print election results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {totalVotes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khanVotes})")
print(f"Correy: {correy_percent:.3f}% ({correyVotes})")
print(f"Li: {li_percent:.3f}% ({liVotes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooleyVotes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")






#output file path to decide where the text document will be sent, I choose the resources folder in PyPoll
output_file = Path('Desktop','python-challenge','PyPoll','Resources','Election_Results_Summary.txt')
with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {totalVotes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khanVotes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correyVotes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({liVotes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooleyVotes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
