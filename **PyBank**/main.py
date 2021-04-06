import os
import csv

csvfile = os.path.join('Resources','budget_data.csv')

#read in csv file
with open (csvfile, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #print(csvreader)

    #skip header row
    csvheader = next(csvfile)
    #print(csvheader)

    #making lists/defining variables
    total_profit_loss = [] 
    row_count = []
    avg_change = []
    greatest_increase = 0
    greatest_increase_month = []
    greatest_decrease = 0
    greatest_decrease_month = []
    total_month_change = 0
    month_change = []
    previous_profit = 0
    date_count = []

    for row in csvreader:
        #caluclating total months
        row_count.append(row)

        #calculating net total amount of "Profit/Losses" over the entire period
        value = (row[1])
        #turning all the values in row[1] from str to int
        x = int(value)
        total_profit_loss.append(x)
        print(total_profit_loss)

        #Change from previous month (subtracting previous number)
        change = int(row[1]) - previous_profit
        month_change.append(change)
        previous_profit = x
        date_count.append(row[0])

        #Greatest increase in profits (date + amount)
        if x > greatest_increase:
            greatest_increase = x
            greatest_increase_month = row[0]
            
        #Greatest decrease in losses (date + amount) 
        if x < greatest_decrease:
            greatest_decrease = x
            greatest_decrease_month = row[0]
        
        #Avg. Change 
        avg_change = sum(month_change)/len(month_change)

    
print("Financial Analysis:")
print("-------------------------------")
print(f"Total Months: {len(row_count)}")
print(f"Total: ${sum(total_profit_loss)}")
print (f"Average Change: {(avg_change)}")
print (f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase}) ")
print (f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease}) ")


#exporting text file
output_file = os.path.join("Analysis", "Analysis.txt")
with open (output_file, 'w') as text_file:
    text_file.write("Financial Analysis:")
    text_file.write("\n-------------------------------")
    text_file.write(f"\nTotal Months: {len(row_count)}")
    text_file.write(f"\nTotal: ${sum(total_profit_loss)}")
    text_file.write(f"\nAverage Change: {(avg_change)}")
    text_file.write(f"\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase}) ")
    text_file.write(f"\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease}) ")