# Steven Pham
# Unit 3 | Assignment - Py Me Up, Charlie
# Option # 1 - pyBank


import os
import csv

# Setting path for  data files
csvpath = os.path.join("budget_data_2.csv")

# Setting up dictionary for holding monthly changes
date_rev = {}

# Setting up variables to hold various counters
month_count = 0 
total_revenue = 0
prior_row = 0
monthly_change = 0
total_change = 0

# Opening budget data csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skipping header    
    next(csvreader)

    for row in csvreader:
        
        # Grabbing current row values
        csvDate = row[0]
        csvRev  = row[1]
        
        # Counting months and summing revenue
        month_count = month_count + 1
        total_revenue = total_revenue + int(csvRev)

        # Calculating monthly change by subtracting row rev vs prior rev
        # Inital value of prior_row is 0. Each loops add current rev to prior_row rev
        monthly_change = int(csvRev) - prior_row 
        prior_row = int(csvRev)

        # To skip first row and properly calculate month to month change
        if(month_count >1):
            date_rev[csvDate] = monthly_change


# Adding up monthly change and avg 
rowSum = (sum(date_rev.values()))
avg = int(rowSum)/int(month_count)

# Grabbing Max value from dictionary
max_date = max(date_rev, key=date_rev.get)
max_rev = date_rev[max_date]

# Grabbing Min value from dictionary
min_date = min(date_rev, key=date_rev.get)
min_rev = date_rev[min_date]


# Output Terminal
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(month_count))
print("Total Revenue: $ " + str(total_revenue))
print("Average Revenue Change: $" + str(int(avg)))
print("Greatest Increase in Revenue: " + str(max_date) + " " + "($ " + str(max_rev) + ")")
print("Greatest Decrease in Revenue: " + str(min_date) + " " + "($ " + str(min_rev) + ")")


## Write the outputs to .txt file
# Specify the file to write to
output_path = os.path.join('pybankOutput.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write to the rows
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow(["Total Months: " + str(month_count)])
    csvwriter.writerow(["Total Revenue: $ " + str(total_revenue)])
    csvwriter.writerow(["Average Revenue Change: $" + str(int(avg))])
    csvwriter.writerow(["Greatest Increase in Revenue: " + str(max_date) + " " + "($ " + str(max_rev) + ")"])
    csvwriter.writerow(["Greatest Decrease in Revenue: " + str(min_date) + " " + "($ " + str(min_rev) + ")"])
