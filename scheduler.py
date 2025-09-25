print("hello")
import random
from typing import List, Tuple

def generate_unique_rounds(team_names: List[str], num_rounds: int = 3) -> List[List[Tuple[str, str]]]:
    """
    Generate rounds of matchups for the given teams with no repeat matchups.
    Each round is a list of (team1, team2) tuples. If odd, one team gets a bye.
    If unable to create a full round without repeats, reshuffle and try again.
    """
    teams = team_names[:]
    n = len(teams)
    all_matchups = set()
    rounds = []
    max_attempts = 100

    for round_num in range(num_rounds):
        attempt = 0
        while attempt < max_attempts:
            random.shuffle(teams)
            round_matchups = []
            used = set()
            valid = True
            for i in range(0, n - 1, 2):
                t1, t2 = teams[i], teams[i + 1]
                matchup = tuple(sorted((t1, t2)))
                if matchup not in all_matchups:
                    round_matchups.append((t1, t2))
                    used.add(t1)
                    used.add(t2)
                else:
                    valid = False
                    break
            # If odd number of teams, one team gets a bye
            if n % 2 == 1:
                bye_found = False
                for t in teams:
                    if t not in used:
                        round_matchups.append((t, None))
                        bye_found = True
                        break
                if not bye_found:
                    valid = False
            if valid and len(round_matchups) == (n // 2) + (n % 2):
                # No repeats and all teams matched
                for match in round_matchups:
                    if match[1] is not None:
                        all_matchups.add(tuple(sorted(match)))
                rounds.append(round_matchups)
                break
            attempt += 1
        else:
            raise ValueError(f"Unable to generate unique matchups for round {round_num+1} after {max_attempts} attempts.")
    return rounds

# with open('rounds/lions.csv', 'rb') as f:
#     reader = csv.reader(f)
#     your_list = list(reader)
# #your_list=your_list[4:]
# for i in your_list:
# 	while len(i)>4:
# 		i.pop(3)
# 	i.pop(0)
# 	i.pop(2)
# del your_list[1::3]
# del your_list[1::2]



# num_teams = len(your_list)
# if num_teams % 2 == 1:
# 	your_list.append(["No team", "Bye"])
# 	num_teams+=1
# l1_indices = random.sample(range(num_teams), num_teams/2)
# l1 = list()
# l2=list()
# for i in range(num_teams):
# 	if i in l1_indices:
# 		l1.append(your_list[i])
# 	else:
# 		l2.append(your_list[i])
# random.shuffle(l1)
# if len(l1) == len(l2):
# 	print("Great success!")
# 	with open('rounds/lions_Round1.csv', 'w') as csvfile:
# 		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
# 		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 		writer.writeheader()
# 		for i in range(num_teams/2):
# 	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[i]), "vs" : "vs" , "Team 2": " ".join(l2[i])})

# 	with open('rounds/lions_Round2.csv', 'w') as csvfile:
# 		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
# 		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 		writer.writeheader()
# 		for i in range(num_teams/2):
# 	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+3)%(num_teams/2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+4)%(num_teams/2)])}) 
# 	with open('rounds/lions_Round3.csv', 'w') as csvfile:
# 		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
# 		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 		writer.writeheader()
# 		for i in range(num_teams/2):
# 	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+13)%(num_teams/2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+15)%(num_teams/2)])}) 
# else:
# 	print("Great success\n\n\nNAAAAAAT!!!")




# with open('rounds/cubs.csv', 'rb') as f:
#     reader = csv.reader(f)
#     your_list = list(reader)
# #your_list=your_list[4:]
# for i in your_list:
# 	while len(i)>4:
# 		i.pop(3)
# 	i.pop(0)
# 	i.pop(2)
# del your_list[1::3]
# del your_list[1::2]

# num_teams = len(your_list)
# if num_teams % 2 == 1:
# 	your_list.append(["No team", "Bye"])
# 	num_teams+=1
# l1_indices = random.sample(range(num_teams), num_teams/2)
# l1 = list()
# l2=list()
# for i in range(num_teams):
# 	if i in l1_indices:
# 		l1.append(your_list[i])
# 	else:
# 		l2.append(your_list[i])
# random.shuffle(l1)
# if len(l1) == len(l2):
# 	print("Great success!")
# 	with open('rounds/cubs_Round1.csv', 'w') as csvfile:
# 		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
# 		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 		writer.writeheader()
# 		for i in range(num_teams/2):
# 	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[i]), "vs" : "vs" , "Team 2": " ".join(l2[i])})

# 	with open('rounds/cubs_Round2.csv', 'w') as csvfile:
# 		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
# 		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 		writer.writeheader()
# 		for i in range(num_teams/2):
# 	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+3)%(num_teams/2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+4)%(num_teams/2)])}) 
# 	with open('rounds/cubs_Round3.csv', 'w') as csvfile:
# 		fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
# 		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 		writer.writeheader()
# 		for i in range(num_teams/2):
# 	   		writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+13)%(num_teams/2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+15)%(num_teams/2)])}) 
# else:
# 	print("Great success\n\n\nNAAAAAAT!!!")