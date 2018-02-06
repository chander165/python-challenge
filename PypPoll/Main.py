import os
import csv
from collections import Counter
csvpath = os.path.join('..','Resources','election_data_1.csv')

unique_list = []
candidates= []
candidate=[]
county = []
voters = []
d = {}
votes = 0
with open(csvpath, newline='') as csvfile:
	next(csvfile)
	csvreader = csv.reader(csvfile, delimiter=',')
	
	for line in csvreader:
		candidates.append(line[2])
		voters.append(line[2])
		votes+=1
	print("Total Votes: "+str(votes)) 
	for item in candidates:
		if item not in candidate:
			candidate.append(item)

	print(dict(Counter(candidates)))
	counter=dict(Counter(candidates))
	vt_cnt=list(counter.values())
	cand=list(counter.keys())
	winner=cand[vt_cnt.index(max(vt_cnt))]
	
	
# Writing to the output File
output_file = os.path.join("pypoll_output.txt")
with open(output_file, 'w') as file_object: 
	file_object.write("Election Results")
	file_object.write("\n-------------------------------")
	file_object.write("\nTotal Votes :"+str(votes))
	file_object.write("\n-------------------------------")
	file_object.write("\n")
	for i in counter:
		file_object.write(i+":"+str(counter[i]/votes*100)+"%"+"("+str(counter[i])+")"+"\n")
	file_object.write("-------------------------------")
	file_object.write("\nWinner is :"+winner)
	file_object.write("\n-------------------------------")

	
	
	
	
	
	
	
	
	
	
