#importing modules to allow csv reading
import os
import csv

#location of the csv file being analyzed 
budget_csv = os.path.join("Resources", "budget_data.csv")

#applying values to variables
total = 0
row_count = 0
profit = 0
largest_value = 0
smallest_value = 0
profit_change = []
month = []
month2 = []
profit_dif = 0


#setting a loop through the csv file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#skipping the header in the loop
    csv_header = next(csv_file)

#assinging more variables a value within the loop 
    first_val = False
    prior_profit = 0
  
#looping through each row   
    for row in csv_reader:
        
#finding total profit and total months in dataset           
        profit = int(row[1])
        row_count += 1
        total += profit
        
#Calculating change in profit each month      
        if first_val == True:
            profit_dif = (profit - prior_profit)
            profit_change.append(profit_dif)
          
#finding largest increase and decrease in profits        
        if profit_dif > largest_value:    
            largest_value = (profit_dif)
            month = row[0]

        if profit_dif < smallest_value:
            smallest_value = (profit_dif)
            month2 = row[0]    
        first_val = True
        prior_profit = profit

        
#Putting together the printed statement of the analysis      
print("Financial Analysis")
print()
print('---------------------------------------')
print()
print(f'Total Months: {row_count}')  
print()      
print(f'Total: ${total}')
print()
print(f'Average Change: ${sum(profit_change)/(row_count-1):.2f}')
print( )
print(f'Greatest Increase in Profits: {month} (${largest_value})')
print()
print(f'Greatest Decrease in Profits: {month2} (${smallest_value})')
print()

#setting a path for a text file to be created then adding text
output_file_path = os.path.join("Analysis","PyBank_Analysis")
with open(output_file_path, 'w') as f:
    print(("Financial Analysis"),file=f)
    print(file=f)
    print(('---------------------------------------'),file=f)
    print(file=f)
    print((f'Total Months: {row_count}'),file=f)  
    print(file=f)      
    print((f'Total: ${total}'),file=f)
    print(file=f)
    print((f'Average Change: ${sum(profit_change)/(row_count-1):.2f}'),file=f)
    print(file=f) 
    print((f'Greatest Increase in Profits: {month} (${largest_value})'),file=f)
    print(file=f)
    print((f'Greatest Decrease in Profits: {month2} (${smallest_value})'),file=f)
    print(file=f)