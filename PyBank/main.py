#Main Program for PyBank
import os
import csv

budget_data =os.path.join("budget_data.csv")


    #initializing 
    
Total_Month = 0
Profit_Value = 0
Total_Loss_Profit = 0
Total_Changes = 0
profit = []
    
date = []

    # calculating Total_month
    #Total_Month +=1
        #print(Total_Month)
   # Total_Loss_Profit += Loss/Profit
      #  #print(Total_Loss_Profit)
     
with open(budget_data_csv) as csv_file:
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
        profit.append(Total_Changes)
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


