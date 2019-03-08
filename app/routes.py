from app import app
from flask import render_template, request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "static/uploaded/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/index')
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/zadanie/58/')
def page():
    return render_template('zadanie58.html')

@app.route('/zadanie/58/', methods=['POST'])
def load_file():
    if request.method == 'POST':
        f1 = request.files['file']
        f2 = request.files['file2']
        f3 = request.files['file3']
        from zbior_zadan.zad58.zad58 import zadanie58
        zadanie58(f1, f2, f3)
        file = open('wyniki.txt', 'r')
        data = file.read()
        file.close()
        data = data.split('\n')
    return render_template('zadanie58.html', data=data)

@app.route('/zadanie/60/')
def page2():
    return render_template('zadanie60.html')

@app.route('/zadanie/60/', methods=['POST'])
def load_file2():
    if request.method == 'POST':
        f = request.files['file']
    from zbior_zadan.zad60.zad60 import zadanie60
    zadanie60(f)
    file = open('wyniki.txt', 'r')
    data = file.read()
    file.close()
    data = data.split('\n')
    return render_template('zadanie60.html', data=data)