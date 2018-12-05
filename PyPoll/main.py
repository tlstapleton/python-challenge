import os
import csv
csvpath = os.path.join('Desktop','PythonStuff', 'python-challenge', 'PyPoll','election_data.csv')
num_voters=0
candidate=[]
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)
    
    numbers=list(csvreader)
    num_voters = len(numbers)
    
    for row in csvreader:
        if row[2] not in candidate:  
            print(row[2])
            candidate.append(row[2])
     
print(candidate)
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {num_voters}")
print(f"----------------------------")
