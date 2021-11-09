"""
Simple "Hello, World" application using Flask
"""

import re
from flask import Flask, request, render_template, flash
from flask.templating import render_template
from mbta_helper import find_stop_near

app = Flask(__name__)



@app.route('/')
def mbta_help():
    return render_template('index.html')
    
@app.route('/result')
def form_input_string(): 
    if request.method == 'GET':
        result = request.form
        find_stop_near(result) #why index error 
        



    


if __name__ == '__main__':
    app.run(debug=True)
