from flask import Flask
from app import app
from flask import render_template
from flask import request
from flask import url_for


@app.route('/')
def home():
    create_link = "<a href= '"+url_for('create')+"'> <h2>Create a Question </h2></a>"
    return """
            <html>
            <head>
                <title> HomePage </title>
                <body> """+ create_link+ """
                </body>
            </head>
            </html>
    """


@app.route('/create')
def create(method=['GET','POST']):
    if request.method == 'GET':
        return render_template('CreateQuestion.html')
    elif request.method == 'POST'
        title     = request.form['title']
        question  = request.form['question']
        answer    = request.form['answer']

        
    else:
        return """
                <h3> Invalid URL </h3>
                """
