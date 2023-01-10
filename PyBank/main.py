#dependencies
import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")
final_analysis = "PyBank"

#set variables#specify the files to read
months = 0
profitloss = 0
change = 0
pllist = 0
date = []
revenue = []

#open budget_data.csv
with open(csvpath)  as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #reading the header row
    csv_header = next(csvreader)

    for row in csvreader:

    #track totals
        months = months + 1
        profitloss = profitloss + int(float(row[1]))

        #track changes and append to lists
        change = int(row[1]) - pllist
        pllist = int(row[1])
        revenue.append(change)
        date.append(row[0])
        
#calculate average change        
avgchange = sum(revenue)/len(revenue)

#least & greatest increase
leastincrease = min(revenue)
leastindex = revenue.index(leastincrease)
leastdate = date[leastindex]
greatestincrease = max(revenue)
greatestindex = revenue.index(greatestincrease)
greatestdate = date[greatestindex]


#Exporing to .txt file & print
output = (
    "\nFinancial Analysis\n"
    "---------------------\n"
    f"Total Months: {str(months)}\n"
    f"Total: ${str(profitloss)}\n"
    f"Average Change: ${str(round(avgchange,2))}\n"
    f"Greatest Increase in Profits: {greatestdate} ${str(greatestincrease)}\n"
    f"Greatest Decrease in Profits: {leastdate} ${str(leastincrease)}\n"
)

print (output)

with open("final_analysis", "w") as txt_file:
    txt_file.write(output)
