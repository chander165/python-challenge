import os
import csv
#from collections import counter
csvpath = os.path.join('..','Resources','election_data_1.csv')

voters= []
county = []

with open(csvpath, newline='') as csvfile:
	next(csvfile)
	csvreader = csv.reader(csvfile, delimiter=',')
	
	cand1 = 0
	cand2 = 0
	cand3 = 0
	cand4 = 0
	for line in csvreader:
		if line[2] == 'Vestal':
			cand1 += 1
		if line[2] == 'Torres':
			cand2 += 1
		if line[2] == 'Seth':
			cand3 += 1
		if line[2] == 'Cordin':
			cand4 += 1
		
total = cand1+cand2+cand3+cand4
print("-----------------------------------------")
print("Election Results")
print("-----------------------------------------")
print("Total Votes :"+str(total))
print("-----------------------------------------")
print("Vestal  :"+str(cand1))
print("Torres  :"+str(cand2))
print("Seth  :"+str(cand3))
print("Cordin  :"+str(cand4))

	
	
	
		
	
	
	
	
	
	
	
	
	
	
