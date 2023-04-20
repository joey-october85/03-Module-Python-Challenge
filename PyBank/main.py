import os
import csv


#working directory PyBank folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#list containing month/date values
months = []

#list containing all the profit/loss values
profitloss = []

#list containing the month to month change values of profit/loss
change_value = []

#set total for all profits/losses to 0
#will be used for running total (calculated in loop)
total = 0

#read in the CSV file
with open(budget_data_csv) as file:

        #split data on commas
        reader = csv.reader(file, delimiter=",")

        csv_header = next(reader)
                
        #loop
        for row in reader:

                #add the value of the 0 index for each row to the months list
                months.append(row[0])
                #add the value of the 1 index for each row to the profitloss list
                profitloss.append(row[1])
                #with each loop the value of the row's profit/loss value will be added to the running total
                total += int(row[1])

              
        #loop - calculate month to month profit/loss change value
        #86 total months but 85 change values exist. (The first row has no previous value to compare against)
        for nr in range(len(months)-1):
                change_value.append(int(profitloss[nr+1]) - int(profitloss[nr]))

        #pull index for greatest profit increase and decrease values
        datemaxindex = change_value.index(max(change_value))
        dateminindex = change_value.index(min(change_value))

        #pull corresponding dates of greatest profit increase and decrease using index (from months list)
        #assign those date strings to their own variable
        datemax = months[datemaxindex]
        datemin = months[dateminindex]

        #calculate change value average and round to two decimals
        change_avg = round(int(sum(change_value))/(int(len(months))-1),2)
        

#print text and results
print("Financial Analysis")
print("----------------------------")
print(f'Total months: {len(months)}')
print(f'Total: ${total}')
print(f'Average Change: ${change_avg}')
print(f'Greatest Increase in Profits: {datemax} $({max(change_value)})')
print(f'Greatest Decrease in Profits: {datemin} $({min(change_value)})')





#write results to a text file in analysis folder
textfile = open('Analysis\\results.txt', 'w')

textfile.write("Financial Analysis \n")
textfile.write("----------------------------\n")
textfile.write(f'Total months: {len(months)}\n')
textfile.write(f'Total: ${total}\n')
textfile.write(f'Average Change: ${change_avg}\n')
textfile.write(f'Greatest Increase in Profits: {datemax} $({max(change_value)})\n')
textfile.write(f'Greatest Decrease in Profits: {datemin} $({min(change_value)})\n')


textfile.close()
