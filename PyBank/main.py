

#import Dependencies
import os
import csv

# read in csv file 
file = os.path.join("/Users/sarahwhite/workspace/python_challenge_repo/python-challenge/PyBank/Resources/budget_data.csv")
with open(file,) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
#create lists to store values 
    month_count = []
    profit = []
    change_profit = []
    
                      
#loop through the values and add them to the associated lists ussing .append methid

    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for x in range(len(profit)-1):
        change_profit.append(profit[x+1]-profit[x])
                      
# create indexes to find increase/decreaase 
increase = max(change_profit)
decrease = min(change_profit)

# Using indexes to find changes 
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

# print out results per instructions 
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      



# Path to output text file
text_path = "budget_analysis.txt"

# write results to ouput text file
with open(text_path, "w") as new :
   new.write("Financial Analysis")
   new.write("\n")
   new.write("------------------------")
   new.write("\n")
   new.write(f"Total Months:{len(month_count)}")
   new.write("\n")
   new.write(f"Total: ${sum(profit)}")
   new.write("\n")
   new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
   new.write("\n")
   new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
   new.write("\n")
   new. write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")
                    
    

