from app import app
from flask import render_template, request
from werkzeug.utils import secure_filename

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
        f1.save(secure_filename(f1.filename))
        f2.save(secure_filename(f2.filename))
        f3.save(secure_filename(f3.filename))
        from zbior_zadan.zad58.zad58 import zadanie58
        zadanie58()
        file = open('systemy_wyniki.txt', 'r')
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
        f.save(secure_filename(f.filename))
    from zbior_zadan.zad60.zad60 import zadanie60
    zadanie60()
    file = open('wyniki.txt', 'r')
    data = file.read()
    file.close()
    data = data.split('\n')
    return render_template('zadanie60.html', data=data)