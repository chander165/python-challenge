import os
import re

word_count =[]
sentances = []
new_count = []
file_open = os.path.join('..','Resources','paragraph_1.txt')

with open(file_open,encoding='utf-8') as file_object:     
	lines = file_object.readlines()
	#print(re.split("(?&lt;=[.!?]) +", file_object))
	
 
	for line in lines: 
		print("this is the line\n"+line)
		count = (re.findall(r'\w+', line))
		new_sent = re.findall(r'\.+',line.replace('\ufeffA','A'))
		#check = re.split("(?&lt;=[.!?]) +", line.replace(u'\ufeff', ''))
		#print(check)
		print("count")
		print(count)
		print("new_sent")
		print(new_sent)
		print('-----------------')
		word_count.append(line.split(' '))
		print("Average Word count in this paragraph :"+ str(len(line.split(' '))))
		print('-----------------')
		sentances.append(line.split('.'))
		print("Approx sentances in the paragraph :"+str(len(line.split('.'))))
		#print((line.split('.')))
		#---------- counting number of letters in each word of the sentence
		y = 0
		for x in count:
			#print(len(x))
			y+=len(x)
		print(y/len(count))
		#----- count of words in sentances
		j=0
		#for a in sentances:
		sentancewordcount = (re.findall(".+", line))
			#for x in range(len(a)):
			#	print((x))
			#print(a.split(' '))
		print(sentancewordcount)
		for a in sentancewordcount:
			print((a))
			j+= len(a)
		print(len(sentances))
		print(j/121)
		


#re.split("(?&lt;=[.!?]) +", paragraph)