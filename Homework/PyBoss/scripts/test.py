import os
import csv
import datetime
csvpath = os.path.join('..','Resources','employee_data1.csv')
first_name = []
last_name = []
dformat = []
state = []
statenew=[]



with open(csvpath, newline='') as csvfile:
	next(csvfile)
	csvreader = csv.reader(csvfile, delimiter=',')
	
	for line in csvreader:
		first_name.append((line[1].split(" "))[0])
		last_name.append((line[1].split(" "))[1])
		from datetime import datetime
		d = datetime.strptime(line[2],'%Y-%m-%d')
		dformat.append(d.strftime('%d/%m/%Y'))
		state.append(line[4])
		for i in state:
			print(i[0:])
		#print(line[4].replace(replace('Florida', 'FL','Alabama', 'AL',
						
		
	

		
