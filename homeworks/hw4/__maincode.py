from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)
filename = 'survey_results.csv'

@app.route('/')
def index():
    return render_template('index.html')

'''@app.route('/thanks')
def thanks():
    return render_template('index.html')

@app.route('/json')
def json():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('index.html')'''

def csvmaker():
    with open(filename, encoding="utf-8") as f:
        f.write('')
if __name__ == "__main__":
    app.run(debug=True)