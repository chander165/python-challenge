import os
import csv
import collections as cs
csvpath = os.path.join('..','Resources','election_data_1.csv')

unique_list = []
voters= []
county = []
d = {}

with open(csvpath, newline='') as csvfile:
	next(csvfile)
	csvreader = csv.reader(csvfile, delimiter=',')
	
	for line in csvreader:
		voters.append(line[2])
		for l in voters:
			d[l] = d.get(l,0) + 1 
#unique candidates with counts
print(d)
		
		#for x in voters:
			#if x in occurrences.keys():
				#occurrences[x] += 1
			#else:
			#	occurrences[x] = 1
	  # check if exists in unique_list or not
			#if x not in unique_list:
				#unique_list.append(x)

#Print(occurrences)
		
			
Print("-------------------------------------------------------------------")		
Print("Election Results")
Print("-------------------------------------------------------------------")		
Print("Total Votes :"+ str(len(voters)))
Print("-------------------------------------------------------------------")		
print("Seth :"+str(voters.count('Seth')*100/len(voters)) + "% ("+	str(voters.count('Seth'))+")"	)
print("Vestal :"+str(voters.count('Vestal')*100/len(voters)) + "% ("+	str(voters.count('Vestal'))+")"	)
print("Cordin :"+str(voters.count('Cordin')*100/len(voters)) + "% ("+	str(voters.count('Cordin'))+")"	)
print("Torres :"+str(voters.count('Torres')*100/len(voters)) + "% ("+	str(voters.count('Torres'))+")"	)
Print("-------------------------------------------------------------------")		
Print("Winner")
print(len(voters))	

	
	
	
	
	
	
	
	
	
	
