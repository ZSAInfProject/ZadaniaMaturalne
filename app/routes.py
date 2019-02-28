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

@app.route('/zadanie/60/')
def page2():
    return render_template('zadanie60.html')

@app.route('/zadanie/60/', methods=['POST'])
def load_file2():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
    from zbior_zadan.zad60.zad60 import zadanie60
    zadanie60()
    file = open('wyniki.txt', 'r')
    data = file.read()
    file.close()
    return data