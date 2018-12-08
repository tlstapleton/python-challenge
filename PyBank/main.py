import os
import csv


csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    next(csvreader, None)
    numbers=[x for x in csvreader]

    for row in csvreader:
         numbers.append(row)

def rolling_difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return diff

x = [row[1] for row in numbers] 
y=  [int(i) for i in x]

total=sum(y)
total_months = len(numbers)

z=rolling_difference(y)

min=0
max=0
for value in z:
    if value<min:
        min=value
    elif value>max:
        max=value


average_change=sum(z)/len(z)
average_change = "%.2f" % average_change
max_month_1= [numbers[z.index(max)+1]]
max_month=[item[0] for item in max_month_1]
min_month_1= [numbers[z.index(min)+1]]
min_month=[item[0] for item in min_month_1]

print("Financial Analysis")
print("----------------------------------------------")
print (f"Total Months: {total_months}")
print (f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f'Greatest Increase in Profits: {max_month} (${max})')
print(f'Greatest Decrease in Profits: {min_month} (${min})')