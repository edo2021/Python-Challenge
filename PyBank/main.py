#Main Program for PyBank
import os
import csv
budget_data_csv =os.path.join("..", "Resources", "budget_data.csv")

def BudgetAnalysis(budgetdata):
    Total_Month = int(budgetdata[0])
    Total_Loss_Profit = float(budgetdata[1])
    Average_Loss_Profit = float(budgetdata[2])
    Max_Loss_profit = float(budgetdata[3])
    Min_Loss_Profit = float(budgetdata[4])
with open(budget_data_csv) as csv_file:
    