import os
import csv


#working directory PyBank folder
budget_data_csv = os.path.join('Resources', 'election_data.csv')

totalvotes = []
candidates = []
candidate_count = [0,0,0]

#read in the CSV file
with open(budget_data_csv) as file:

    #split data on commas
    reader = csv.reader(file, delimiter=",")

    csv_header = next(reader)
    #print(f"CSV Header: {csv_header}")

    for row in reader:
        totalvotes.append(row[0])
        #candidates.append(row[2])
            
        #add all unique candidate values to candidate list
        if str(row[2]) not in candidates:
            candidates.append(row[2])
            
        #count all instances of candidate[0]
        if str(row[2]) == str(candidates[0]):
            candidate_count[0] +=1
        #count all instances of candidate[1]
        elif str(row[2]) == str(candidates[1]):
            candidate_count[1] +=1
        #count all instances of candidate[1]
        elif str(row[2]) == str(candidates[2]):
            candidate_count[2] +=1
          
winnerindex = candidate_count.index(max(candidate_count))
winner = candidates[winnerindex]

print("Election Results \n" + "-------------------------")
print(f'Total Votes: {len(totalvotes)}')
print("-------------------------")
for candidate_index in range(len(candidates)):
    can_count = str(candidate_count[candidate_index])
    can_name = str(candidates[candidate_index])
    can_avg = int(candidate_count[candidate_index])/sum(candidate_count)

    print(f'{can_name} {can_avg: .3%} ({can_count})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")


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