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
    # Conduct the ask
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])