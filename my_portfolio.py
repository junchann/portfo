
#! MY PORTFOLIO

from flask import Flask, render_template, redirect
import webbrowser
from requests import request
from flask import request
import csv


app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('/Users/junchan/Documents/VsCode/PYTHON/webdevelopment/venv/database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')
        return file

def write_to_csv(data):
    with open('/Users/junchan/Documents/VsCode/PYTHON/webdevelopment/venv/database.csv', 'a', newline= '') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return render_template('thankyou.html') #* or we can use redirect('./thank_you.html') 
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, please try again'
    


