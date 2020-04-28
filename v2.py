import shutil

from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import os, csv, random, zipfile
import pandas as pd

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'xlsx', 'xls'}


def allowed_file(filename):
    print(filename.rsplit('.', 1)[1])
    allowed = '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    return allowed


def write_to_csv(rounds, round_num, group_name):
    file_path = "./downloads/" + group_name + "_" + round_num + ".csv"
    with open(file_path, 'w') as csv_file:
        fieldnames = ["Room Number", "Team 1", "vs", "Team 2"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(rounds)):
            writer.writerow({"Room Number": rounds[i][0], "Team 1": " ".join([rounds[i][1]]), "vs": "vs",
                             "Team 2": " ".join([rounds[i][2]])})


def make_round(teams_a, teams_b, already_matched):
    random.shuffle(teams_a)
    random.shuffle(teams_b)
    teams_b_used = list()
    rounds = list()
    room_number = 1
    for i in teams_a:
        for j in teams_b:
            if j not in teams_b_used and j not in already_matched[i]:
                if j != "No Team, Bye":
                    rounds.append([room_number, i, j])
                    room_number += 1
                else:
                    rounds.append(["No room", i, j])
                already_matched[i].append(j)
                teams_b_used.append(j)
                break
    return rounds


def do_stuff(df, num_rounds, group_name):
    df.drop([df.columns[0]], axis='columns', inplace=True)
    df.drop([0, 1, 2, 3], inplace=True)
    df = df[df[3] == df[3]]
    team_codes = df[2].tolist()
    team_names = df[3].tolist()
    teams = list()
    for i in range(len(team_names)):
        if team_names[i].strip() != "":
            teams.append(team_codes[i].strip() + " " + team_names[i].strip())
    teams = list(set(teams))
    random.shuffle(teams)
    if len(teams) % 2 != 0:
        teams.append("No Team, Bye")
    half_teams = int(len(teams) / 2)
    teams_a = teams[:half_teams]
    teams_b = teams[half_teams:]
    already_matched = dict()
    for i in teams_a:
        already_matched[i] = list()
    for i in range(num_rounds):
        rounds = make_round(teams_a, teams_b, already_matched)
        write_to_csv(rounds, "round_" + str(i+1), group_name)


def generate_rounds(filename, num_rounds):
    if os.path.exists("./downloads"):
        shutil.rmtree("./downloads")
        os.mkdir("./downloads")
        filepath = './uploads/' + str(filename)
        xls = pd.ExcelFile(filepath)
        df1 = pd.read_excel(xls, 'Lions Registration', header=None)
        df2 = pd.read_excel(xls, 'Cubs Registration', header=None)
        do_stuff(df1, num_rounds, "lions")
        do_stuff(df2, num_rounds, "cubs")


@app.route('/')
def login():
    print("hello world")
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        num_rounds = int(request.form["num_rounds"])
        if num_rounds<1:
            raise Exception("invalid number of rounds entered")
        print(num_rounds)
        if f and allowed_file(f.filename):
            curpath = os.path.abspath(os.curdir)
            print("Current path is: %s", (curpath))
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            generate_rounds(filename, num_rounds)
            zipf = zipfile.ZipFile('Rounds.zip', 'w', zipfile.ZIP_DEFLATED)
            for root, dirs, files in os.walk('./downloads/'):
                for file in files:
                    zipf.write('./downloads/' + file)
            zipf.close()
            return send_file('Rounds.zip', mimetype='zip', attachment_filename='Rounds.zip', as_attachment=True)
        else:
            raise Exception("Something went wrong. please contact a dev")

if __name__ == '__main__':
    app.run(debug=True)
