#By Edris Gemtessa University of Minnesot
#main program

import os
import csv

 # Set the path for the CSV file 

PyPollcsv = os.path.join("Resources","election_data.csv")

#Create the lists to store data. 


candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

#create variable and initalize
count = 0

#open the CSV using to read and create for loo

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #read the csv file from all row
    for row in csvreader:

        # Count the total number of votes
        count = count + 1
        # append candidate names list 
        candidatelist.append(row[2])

    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)

        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]




print("-------------------------")
print("Election Analysis Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] +   ": "+           str(round(vote_percent[i],1)) +"00 %           ("       + str(vote_count[i])+   ")")



print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


with open('election_Data_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("--------------------------------------")