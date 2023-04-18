import os
import csv


#working directory PyBank folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#list for total months     
totalmonths = []

#list for month to month value change
valuechange = []


#set total for all profits/losses to 0
#will be used for running sum (calculated in loop)
total = 0

#value for month to moth profit/loss change. Initially set to 0 and recalculated in loop
change = 0

#read in the CSV file
with open(budget_data_csv) as file:

        #split data on commas
        reader = csv.reader(file, delimiter=",")

        csv_header = next(reader)
        #print(f"CSV Header: {csv_header}")
        
        #create loop to read each row
        for row in reader:

                #add the value of the 0 index for each row to the total months list
                #this will add the date string to the totalmonths list created above
                totalmonths.append(row[0])

                #with each loop the value of the row's profit/loss value will be added to the running sum
                total += int(row[1])

                #calculate profit/loss change value
                #assign the value of the profit/loss for the row to adjustedchange variable
                adjustedchange = int(row[1])
                #take the value of our change value and subtrace adjusted change
                change -= adjustedchange
                #add the change value to valuechange list created above
                valuechange.append(change)
                #redefine value of change for the next loop
                change = int(row[1])

        #establish values for calculating average change value        
        ignore = valuechange[0]
        valuechangecount = len(valuechange) - 1
        valuechangesum = ignore - sum(valuechange)
        valuechangeavg = round(valuechangesum/valuechangecount,2)

        #pull index for greatest profit increase and decrease values
        datemaxindex = valuechange.index(max(valuechange))
        dateminindex = valuechange.index(min(valuechange))

        #pull corresponding dates of greatest profit increase and decrease using index (from totalmonths list)
        #assign those date strings to their own variable
        datemax = totalmonths[datemaxindex]
        datemin = totalmonths[dateminindex]

#print text and results
print("Financial Analysis")
print("----------------------------")
print(f'Total months: {len(totalmonths)}')
print(f'Total: ${total}')
print(f'Average Change: ${valuechangeavg}')
print(f'Greatest Increase in Profits: {datemax} $({max(valuechange)})')
print(f'Greatest Decrease in Profits: {datemin} $({min(valuechange)})')




#write results to a text file in analysis folder
textfile = open('Analysis\\results.txt', 'w')

textfile.write("Financial Analysis \n")
textfile.write("----------------------------\n")
textfile.write(f'Total months: {len(totalmonths)}\n')
textfile.write(f'Total: ${total}\n')
textfile.write(f'Average Change: ${valuechangeavg}\n')
textfile.write(f'Greatest Increase in Profits: {datemax} $({max(valuechange)})\n')
textfile.write(f'Greatest Decrease in Profits: {datemin} $({min(valuechange)})\n')


textfile.close()
