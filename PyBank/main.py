#Main Program for PyBank
import os
import csv

budget_data =os.path.join("Resources","budget_data.csv")

#List Created for storing Data
Monthly_changes = []
profit = []
date = []
    #initializing 

count = 0
initial_Profit = 0
Profit_Value = 0
Total_Change_Profit = 0
total_profit = 0


    # calculating Total_month
    #Total_Month +=1
        #print(Total_Month)
   # Total_Loss_Profit += Loss/Profit
      #  #print(Total_Loss_Profit)
     
     #opening the file for reading
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Reading the header Row
    csv_header = next(csvreader)
    first_row = next(csvreader)
    Total_Month += 1
    Total_Loss_Profit = int(first_row[1])
    Profit_Value = int(first_row[1])

    for row in csvreader:

        dates.append(row[0])
        Total_Changes = int(row[1]-Profit_Value
        profit.append(row[1])
        Profit_Value = int(row[1])

        Total_Month += 1
        Total_Loss_Profit = Total_Loss_Profit + int(row[1])

        # Calculating the Greatest increase and decrease

    Greatest_increase = max(profit)
    Greatest_decrease = min(profit)

    Average_Changes = sum(profit)/len(profits)

    print(Total_Month)
    print(Total_Loss_Profit)
    print(Greatest_increase)
    print(Geatest_decrease)


