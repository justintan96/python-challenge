
#PART A: starting codes to read in my csv file to do my data analysis 
# import 

import os
import csv

# path to collect data from csv and open the csv file to conduct analysis 

budget_csv = os.path.join("Resources","budget_data.csv")
os.getcwd()
# With open is a command that opens up your csv file so that when you do your analysis it is able to reference the file, without opening python can't read it 
#Ensure you always indent your code after "with open" or it will automatically close the file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# read first line as hader 
    csv_header = next(csvfile)

# PART B setting up my variables as a starting point of calculation and list necessary to hold information 

 #set my variables up   
    count = 0
    total_profit = 0 
    start_profit = 0
    sum_change_profit = 0
#set up list to hold the changes in profit data and store dates 
    monthly_change = []
    date = []
    profit = []
   
   
#this is to calculate my amount of months in my csv file, where count starts at 0, for each subsequent row add 1
    for row in csvreader:
        count = count + 1
# In the list i created in part B, append the data of rows [0,1] in it, i am essentially creating a new list and storing the csv data into it 
        date.append(row[0])

# find total profits, we are taking the start value (0) and adding on the values in the profit/loss column row[1]
        total_profit = total_profit + int(row[1])
# average of the changes in profit/losses over the period
  
        final_profit = int(row[1])
        month_profit = final_profit - start_profit
# after calculating the change in monthly profit, append the data into a new list monthly_changes 

        monthly_change.append(month_profit)
        change_profit = sum_change_profit + month_profit 

# I'm not sure why we do start = final QUESTION

        start_profit = final_profit
        average_profit = (change_profit/count)

# greatest increase and decrease in profits/losses (date and amount) over entire period/months
        greatest_increase_profit = max(monthly_change)
        greatest_decrease_profit = min(monthly_change)
# we are indexing/finding the month of the greatest changes in profit (highest and lowest)
        greatest_increase_date = date[monthly_change.index(greatest_increase_profit)]
        greatest_decrease_date = date[monthly_change.index(greatest_decrease_profit)]
    
# once complete print the analysis to the terminal and export text file with results 
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Profit Change: " + "$" + str(average_profit))
    print("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase_profit) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease_profit)+ ")")

# write my results into a textfile 

with open('PyBank_answers.txt', 'w') as f:
    f.write("Total Months: " + str(count) + "\n")
    f.write("Total Profits: " + "$" + str(total_profit) + "\n")
    f.write("Average Profit Change: " + "$" + str(average_profit) + "\n")
    f.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase_profit) + "\n")
    f.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease_profit) + "\n")

    f.close() 