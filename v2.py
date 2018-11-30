from flask import Flask, render_template

app = Flask(__name__)

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['.xlsx'])


@app.route('/')
def login():
    return render_template('index.html')

