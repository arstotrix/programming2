from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)
filename = 'survey_results.csv'
correct = ['council','capital','stationary','descent','effects','complements','lose','capitol','stationery','dissent','affect','counsel']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thanks', methods = ['POST', 'GET'])
def thanks():
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        level = request.form['level']
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        q6 = request.form['q6']
        q7 = request.form['q7']
        q8 = request.form['q8']
        q9 = request.form['q9']
        q10 = request.form['q10']
        q11 = request.form['q11']
        q12 = request.form['q12']
        fin_form = 'Thank you for your patience (and your answers)'
        fieldnames = ['gender', 'age', 'level', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12']
        with open(filename, 'a+', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'gender': gender, 'age': age, 'level': level, 'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'q6': q6, 'q7': q7, 'q8': q8, 'q9': q9, 'q10': q10, 'q11': q11, 'q12': q12 })
    return render_template('thanks.html', fin_form=fin_form)


'''@app.route('/json')
def json():
    return render_template('json.html')

@app.route('/stats')
def results():
    return render_template('stats.html')
    
@app.route('/correct')
def results():
    return render_template('correct.html')

@app.route('/search')
def search():
    if request.method='POST'
        
    return render_template('search.html')

@app.route('/results')
def results():
    return render_template('results.html')'''

if __name__ == "__main__":
    app.run(debug=True)