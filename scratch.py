import pandas as pd
import random
import os, shutil
import csv

def write_to_csv(rounds, round_num, group_name):
    file_path = "./output/"+group_name+"_"+round_num+".csv"
    with open(file_path,'w') as csv_file:
        fieldnames = ["Room Number", "Team 1", "vs", "Team 2"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(rounds)):
            writer.writerow({"Room Number": rounds[i][0], "Team 1": " ".join([rounds[i][1]]), "vs": "vs", "Team 2": " ".join([rounds[i][2]])})

def make_round(teams_a, teams_b, already_matched):
    random.shuffle(teams_a)
    random.shuffle(teams_b)
    teams_b_used = list()
    rounds = list()
    room_number = 1
    for i in teams_a:
        for j in teams_b:
            if j not in teams_b_used and j not in already_matched[i]:
                rounds.append([room_number,i,j])
                already_matched[i].append(j)
                room_number+=1
                teams_b_used.append(j)
                break
    return rounds

def do_stuff(df, num_rounds, group_name):
    df.drop([df.columns[0]], axis='columns', inplace=True)
    df.drop([0,1,2,3], inplace=True)
    df = df[df[3]==df[3]]
    team_codes = df[2].tolist()
    team_names = df[3].tolist()
    teams = list()
    for i in range(len(team_names)):
        if team_names[i].strip()!="":
            teams.append(team_codes[i].strip() + " " + team_names[i].strip())
    teams = list(set(teams))
    if len(teams) % 2 != 0:
        teams.append("No Team, Bye")
    half_teams = int(len(teams)/2)
    random.shuffle(teams)
    teams_a = teams[:half_teams]
    teams_b = teams[half_teams:]
    already_matched=dict()
    for i in teams_a:
        already_matched[i]=list()
    for i in range(num_rounds):
        rounds = make_round(teams_a, teams_b, already_matched)
        write_to_csv(rounds, "round_"+str(i), group_name)





xls = pd.ExcelFile('/home/bolshack/Downloads/Dwarka 2 Tournament Template November 2019.xlsx')
if os.path.exists("./output"):
    shutil.rmtree("./output")
os.mkdir("./output")
df1 = pd.read_excel(xls, 'Lions Registration', header=None)
df2 = pd.read_excel(xls, 'Cubs Registration', header=None)
do_stuff(df1, 3, "lions")
do_stuff(df2, 3, "cubs")
