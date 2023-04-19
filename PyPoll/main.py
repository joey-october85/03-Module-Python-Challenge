import os
import csv


#working directory PyBank folder
budget_data_csv = os.path.join('Resources', 'election_data.csv')

#lists containing values for votes, candidates 
totalvotes = []
candidates = []

#total votes for each candidate. Initially set to 0 and tallied in the loop
candidate_count = [0,0,0]

#read in the CSV file
with open(budget_data_csv) as file:

    #split data on commas
    reader = csv.reader(file, delimiter=",")

    csv_header = next(reader)

    #loop
    for row in reader:
        #append the values of all votes to the totalvotes list
        totalvotes.append(row[0])
                    
        #append all unique candidate values to candidate list
        if str(row[2]) not in candidates:
            candidates.append(row[2])

        #count each instance of votes cast per candidate to get total votes for each candidate    
        #count all votes for candidate[0] and add to candidate_count list
        if str(row[2]) == str(candidates[0]):
            candidate_count[0] +=1
        #count all votes for candidate[1] and add to candidate_count list
        elif str(row[2]) == str(candidates[1]):
            candidate_count[1] +=1
        #count all votes for candidate[1] and add to candidate_count list
        elif str(row[2]) == str(candidates[2]):
            candidate_count[2] +=1

#find winner: identify the max value from the candidate_count list - store the index
winnerindex = candidate_count.index(max(candidate_count))
#pull winner from candidates list using winnerindex above
winner = candidates[winnerindex]

#print text and results
print("Election Results \n" + "-------------------------")
print(f'Total Votes: {len(totalvotes)}')
print("-------------------------")
#create loop to cycle through lists to pull candidate info/results and print each one in their own row
for candidate_index in range(len(candidates)):
    can_count = str(candidate_count[candidate_index])
    can_name = str(candidates[candidate_index])
    can_avg = int(candidate_count[candidate_index])/sum(candidate_count)

    print(f'{can_name} {can_avg: .3%} ({can_count})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

#output results to textfile
textfile = open('Analysis\\results.txt', 'w')

textfile.write("Election Results \n" + "-------------------------\n")
textfile.write(f'Total Votes: {len(totalvotes)}\n')
textfile.write("-------------------------\n")
for candidate_index in range(len(candidates)):
    can_count = str(candidate_count[candidate_index])
    can_name = str(candidates[candidate_index])
    can_avg = int(candidate_count[candidate_index])/sum(candidate_count)

    textfile.write(f'{can_name} {can_avg: .3%} ({can_count})\n')
textfile.write("-------------------------\n")
textfile.write(f'Winner: {winner}\n')
textfile.write("-------------------------\n")

textfile.close()