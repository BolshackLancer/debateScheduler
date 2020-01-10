from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import os, csv, random, zipfile

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
	print(filename.rsplit('.',1)[1])
	allowed = '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
	#print(x)
	return allowed

def generate_rounds(filename):
	filepath = './uploads/'+str(filename)
	with open(filepath, 'r', encoding = "latin-1") as f:
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
	l1_indices = random.sample(range(num_teams), num_teams//2)
	l1 = list()
	l2=list()
	for i in range(num_teams):
		if i in l1_indices:
			l1.append(your_list[i])
		else:
			l2.append(your_list[i])
	random.shuffle(l1)
	if len(l1) == len(l2):
		with open('./downloads/Round1.csv', 'w') as csvfile:
			fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for i in range(num_teams//2):
				writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[i]), "vs" : "vs" , "Team 2": " ".join(l2[i])})

		with open('./downloads/Round2.csv', 'w') as csvfile:
			fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for i in range(num_teams//2):
				writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+3)%(num_teams//2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+4)%(num_teams//2)])}) 
		with open('./downloads/Round3.csv', 'w') as csvfile:
			fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for i in range(num_teams//2):
				writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+13)%(num_teams//2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+15)%(num_teams//2)])}) 
		with open('./downloads/Round4.csv', 'w') as csvfile:
			fieldnames = ["Room Number" ,"Team 1","vs", "Team 2"]
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for i in range(num_teams//2):
				writer.writerow({"Room Number" : i+1, "Team 1" : " ".join(l1[(i+13)%(num_teams//2)]), "vs" : "vs" , "Team 2": " ".join(l2[(i+20)%(num_teams//2)])}) 	
			
			return "Great success!"
	return "Great success\n\n\nNAAAAAAT!!!"

@app.route('/')
def login():
	print("hello world")
	return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	#print("In uploader function")
	if request.method == 'POST':
		f = request.files['file']
		if f:
			print("f")
		if allowed_file(f.filename):
			print("allowed_file")
		if f and allowed_file(f.filename):
			curpath = os.path.abspath(os.curdir)
			print ("Current path is: %s", (curpath))
			filename = secure_filename(f.filename)
			f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			#return redirect(url_for('index'))
			if generate_rounds(filename) == "Great success!":
				zipf = zipfile.ZipFile('Rounds.zip','w', zipfile.ZIP_DEFLATED)
				for root,dirs, files in os.walk('./downloads/'):
					for file in files:
						zipf.write('./downloads/'+file)
				zipf.close()
				return send_file('Rounds.zip',mimetype = 'zip', attachment_filename= 'Rounds.zip',as_attachment = True)

		return "File upload unsuccessful"

if __name__ == '__main__':
	app.run(debug = True)