import os
import csv
csvpath = os.path.join('Resources','budget_data_1.csv')
revenuesum=[]
sumint=[]
months=[]
unique_list = []
not_unique_list = []
new_months = []
dates = []

with open(csvpath, newline='') as csvfile:
	next(csvfile)
	csvreader = csv.reader(csvfile, delimiter=',')
	#lines = csvfile.read()
	#print(lines)
	for line in csvreader:
		months.append((line[0].split("-"))[0])
		dates.append(line[0])
		revenuesum.append(int(line[1]))
		#revenuesum += revenuesum
	arraytotal = 0
	for i in range(len(revenuesum)):
		arraytotal += revenuesum[i]
		sumint.append(revenuesum[i]-revenuesum[i-1])
				
	    # traverse for all elements

##----- Finding Unique Months from the list
	for x in months:
	  # check if exists in unique_list or not
		if x not in unique_list:
			unique_list.append(x)
			#print("The unique Months are"+unique_list[x])
	
print((unique_list))
print("Total unique months"+str(len(unique_list)))
print("Total Revenue is :$"+str(arraytotal))
print("The average revenue is :$"+str(arraytotal/len(revenuesum)))
print("this date has the greatest change :"+dates[sumint.index(max(sumint))]+" with amount $"+str(max(sumint)))
print("this date has the least change :"+dates[sumint.index(min(sumint))]+" with amount $"+str(min(sumint)))

# Writing to the output File
output_file = os.path.join("pybank_output.txt")
with open(output_file, 'w') as file_object:     
	file_object.write("Total unique months :"+str(len(unique_list))) 
	file_object.write("\nTotal Revenue is :"+str(arraytotal)) 
	file_object.write("\nThe average revenue is :"+str(arraytotal/len(revenuesum)))
	file_object.write("\nthis date has the greatest change :"+dates[sumint.index(max(sumint))]+" with amount $"+str(max(sumint)))
	file_object.write("\nhis date has the least change :"+dates[sumint.index(min(sumint))]+" with amount $"+str(min(sumint)))

	
	#with open(csvpath, 'r') as file_handler:
	#
	#
    
	#"""Add two numbers and return the sum."""
		
 
