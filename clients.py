
import csv

file = open('clients.csv','r')
reader = csv.reader(file)

dic = {}
for item in reader:
	if reader.line_num == 1:
		continue
	month = item[2][:7]
	if month not in dic.keys():
		dic[month] = []
	dic[month].append(item[1])

most = 0
max_month = ''
for (month,names) in dic.items():
	counter = len(list(set(names)))
	if counter == most:
		max_month = max_month + ' '+ month
		
	if counter > most:
		most = counter
		max_month = month
	

print('Month with most clients: ',max_month,'clients number: ', most)





		
