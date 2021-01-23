#Main Program for PyBank
import os
import csv

budget_data_csv =os.path.join("Resources","budget_data.csv")

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
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Reading the header Row
    csv_header = next(csvreader)
    #first_row = next(csvreader)

    #Total_Month += 1
    #Total_Loss_Profit = int(first_row[1])
    #Profit_Value = int(first_row[1])

    for row in csvreader:
        count = count + 1

        date.append(row[0])
        #Total_Changes = int(row[1]-Profit_Value
        profit.append(row[1])
        total_profit = total_profit +int(row[1])

        #calculate average changes
        final_profit = int(row[1])
        Monthly_change_Profits = final_profit - initial_Profit
        #Store monthly changes in the list
        Monthly_changes.append(Monthly_change_Profits)
#calculate Total_Change_Profit and assign final profit to initial profit for next row
        Total_Change_Profit = Total_Change_Profit + Monthly_change_Profits

        initial_Profit = final_profit

        #Calculate average change
        Average_Changes_profit = Total_Change_Profit/count


        #Profit_Value = int(row[1])

        #Total_Month += 1
        #Total_Loss_Profit = Total_Loss_Profit + int(row[1])

        # Calculating the Greatest increase and decrease

    Greatest_increase = max(profit)
    Greatest_decrease = min(profit)

    Average_Changes = sum(profit)/len(profits)

    print(count)
    print(total_profit)
    print(Greatest_increase)
    print(Greatest_decrease)


