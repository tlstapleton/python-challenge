import os
import csv
csvpath = os.path.join('Desktop','PythonStuff', 'python-challenge', 'PyBank','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    next(csvreader, None)
    numbers=[x for x in csvreader]

    for row in csvreader:
         numbers.append(row)

def column(matrix,i):
    return [row[i] for row in matrix]

def rolling_difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return diff

x = column(numbers,1) 
y=[int(i) for i in x]

min=0
max=0
for i in y:
    if i<min:
        min=i
    elif i>max:
        max=i

min_month = column([i for i in numbers if str(min) in i],0)
max_month = column([i for i in numbers if str(max) in i],0)

total=sum(y)
total_months = len(numbers)

z=rolling_difference(y)
average_change=sum(z)/len(z)
average_change = "%.2f" % average_change

print("Financial Analysis")
print("----------------------------------------------")
print (f"Total Months: {total_months}")
print (f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f'Greatest Increase in Profits: {max_month} (${max})')
print(f'Greatest Decrease in Profits: {min_month} (${min})')