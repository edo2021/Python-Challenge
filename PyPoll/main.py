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
