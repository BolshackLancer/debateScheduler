print("hello")
import csv
import random
with open('rounds/lions.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
#your_list=your_list[4:]
for i in your_list:
	while len(i)>4:
		i.pop(3)
	i.pop(0)
	i.pop(2)
del your_list[1::3]
del your_list[1::2]



num_teams = len(your_list)
if num_teams % 2 == 1:
	your_list.append(["No team", "Bye"])
	num_teams+=1
l1_indices = random.sample(range(num_teams), num_teams/2)
l1 = list()
l2=list()
for i in range(num_teams):
	if i in l1_indices:
		l1.append(your_list[i])
	else:
		l2.append(your_list[i])
random.shuffle(l1)
if len(l1) == len(l2):
	print("Great success!")
	with open('rounds/lions_Round1.csv', 'w') as csvfile:
		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for i in range(num_teams/2):
	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[i]), "vs" : "vs" , "Team 2": " ".join(l2[i])})

	with open('rounds/lions_Round2.csv', 'w') as csvfile:
		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for i in range(num_teams/2):
	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+3)%(num_teams/2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+4)%(num_teams/2)])}) 
	with open('rounds/lions_Round3.csv', 'w') as csvfile:
		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for i in range(num_teams/2):
	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+13)%(num_teams/2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+15)%(num_teams/2)])}) 
else:
	print("Great success\n\n\nNAAAAAAT!!!")




with open('rounds/cubs.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
#your_list=your_list[4:]
for i in your_list:
	while len(i)>4:
		i.pop(3)
	i.pop(0)
	i.pop(2)
del your_list[1::3]
del your_list[1::2]

num_teams = len(your_list)
if num_teams % 2 == 1:
	your_list.append(["No team", "Bye"])
	num_teams+=1
l1_indices = random.sample(range(num_teams), num_teams/2)
l1 = list()
l2=list()
for i in range(num_teams):
	if i in l1_indices:
		l1.append(your_list[i])
	else:
		l2.append(your_list[i])
random.shuffle(l1)
if len(l1) == len(l2):
	print("Great success!")
	with open('rounds/cubs_Round1.csv', 'w') as csvfile:
		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for i in range(num_teams/2):
	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[i]), "vs" : "vs" , "Team 2": " ".join(l2[i])})

	with open('rounds/cubs_Round2.csv', 'w') as csvfile:
		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for i in range(num_teams/2):
	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+3)%(num_teams/2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+4)%(num_teams/2)])}) 
	with open('rounds/cubs_Round3.csv', 'w') as csvfile:
		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for i in range(num_teams/2):
	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+13)%(num_teams/2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+15)%(num_teams/2)])}) 
else:
	print("Great success\n\n\nNAAAAAAT!!!")