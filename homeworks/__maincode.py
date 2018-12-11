from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)
filename = 'flresults.csv'

def csvmakerr():
    with open() as f:
        f.write('')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thanks', methods = ['POST', 'GET'])
def thanks_file():
    if request.method == 'POST':
        ask = request.form['ask']
        what = request.form['what']
        how = request.form['how']
        name = request.form['name']
        surname = request.form['surname']
        fin_form = "Спасибо за ответ!"
        fieldnames = ['ask','what','how','name','surname']
        with open(filename, 'a+', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'ask':ask, 'what':what, 'how':how, 'name':name, 'surname':surname})
        return render_template('thanks.html', fin_form=fin_form)

'''@app.route('/')
def index():
    return render_template('index.html')

@app.route('/json')
def index():
    return render_template('index.html')

@app.route('/search')    
def index():
    return render_template('search.html')

@app.route('/results')
def index():
    return render_template('index.html')    
'''

if __name__ == '__main__':
    app.run(debug=True)
