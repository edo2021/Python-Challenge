#Edris Gemtessa, University of Minnesota
# This is Main program 
import os
import csv 

#Gettting the file Path

Budget_datacsv = os.path.join("Resource","budget_data.csv")

#List to store Data
profit = []
monthly_changes = []
date = []

 #creating and Initialize the variables 
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Opening the csv file from the path for reading

with open (Budget_datacsv) as csvfile:
    csvreader = csv.reader(csvfile, delimite = ",")

    # Reading the heeading
    cvs_header = next(csvreader)

    # for loop to append List and to calculate the variables
    for row in csvreader:
        count = count + 1
        date.append(row[0])
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        final_profit = int(row[1])

        monthly_change_profits = final_profit - initial_profit
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        average_change_profits = (total_change_profits/count)






