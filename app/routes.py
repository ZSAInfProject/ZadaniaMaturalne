from app import app
from flask import render_template, request
from werkzeug.utils import secure_filename

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/zadanie/58/')
def page():
    return render_template('zadanie58.html')

@app.route('/zadanie/58/', methods=['POST'])
def load_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
    return "" + f.filename