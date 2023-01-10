#dependencies
import os
import csv

#specify the files to read & write
csvpath = os.path.join("Resources", "election_data.csv")
poll_analysis = "PyPoll"

#set variables
votes = 0
candidates = []
candidatevotes = {}
candidatepercent = []

#open election_data.csv
with open(csvpath)  as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #reading the header row
    csv_header = next(csvreader)

    for row in csvreader:

        #track total votes
        votes = votes + 1
        candidate = row[2]

#get single candidate list
if candidate not in candidates:

    candidates.append(candidate)
    candidatevotes[candidate] = 0

candidatevotes[candidate] = candidatevotes[candidate] + 1
        
    
for candidate in candidatevotes:

    #get votes & percentage by candidate
    totalvotes = candidatevotes.get(candidate)
    percent = float(totalvotes) / float(totalvotes) * 100

#get top vote count
topvotes = max(candidatevotes)
winner = candidatevotes.get(candidate)


#export to .txt file & print
output = (
    "\nElection Results\n"
    "---------------------\n"
    f"Total Votes: {str(votes)}\n"
    "---------------------\n"
    f"{candidate}: {percent:.1f}% ({totalvotes:,})\n"
    "---------------------\n"
    f"{str(winner)}\n"
    "---------------------\n"
)

print (output)

with open("poll_analysis", "w") as txt_file:
    txt_file.write(output)