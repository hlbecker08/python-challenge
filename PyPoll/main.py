#settin up modules to let us read csv file
import os
import csv

#selecting the path to the csv file
election_csv = os.path.join("Resources", "election_data.csv")

#assinging values to variables
total_votes = 0
candidates = []
voting = {}

#starting loop through csv file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
#skipping firt row of csv file 
    csv_header = next(csv_file)

#starting a loop through all rows in the dataset
    for row in csv_reader:

#collecting names of candidates and total votes        
        candidates.append(row[2])
        total_votes += 1

#applying a vote count to each indiviudal candidate 
    for name in candidates:
        if name in voting:
            voting[name] += 1

        else:
            voting[name] = 1

#setting variables for winner
high_vote = 0
winner = ""

#creating print statement with analysis results
print()
print("Election Results")
print()
print("--------------------------------------")
print()
print(f'Total Votes: {total_votes}')
print()
print("--------------------------------------")
print()
#finding winner of the election
for key, value in voting.items():
    if value > high_vote:
        winner = key
        high_vote = value
    print(f'{key}: {(value/total_votes)*100:.3f}% ({value})')
    print()
print("--------------------------------------") 
print()
print(f'Winner: {winner}')
print()
print("--------------------------------------")

#seting output path for text file and what is to be printed
output_file_path = os.path.join("Analysis","PyPoll_Analysis")
with open(output_file_path, 'w') as f:
    print(file=f)
    print(("Election Results"),file=f)
    print(file=f)
    print(("--------------------------------------"),file=f)
    print(file=f)
    print((f'Total Votes: {total_votes}'),file=f)
    print(file=f)
    print(("--------------------------------------"),file=f)
    print(file=f)
    for key, value in voting.items():
        if value > high_vote:
            winner = key
            high_vote = value
        print((f'{key}: {(value/total_votes)*100:.3f}% ({value})'),file=f)
        print(file=f)
    print(("--------------------------------------"),file=f)
    print(file=f)
    print((f'Winner: {winner}'),file=f)
    print(file=f)
    print(("--------------------------------------"),file=f)
