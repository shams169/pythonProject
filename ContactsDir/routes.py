# server /

from flask import Flask
#from ContactsDir.app import app
from app import app

@app.route('/')
def myname():
    str = """
    <html>
    <title>Hello World </title>
    <body>
        <h1>This is the first page in Flask</h1>
    </body>

    </html>2
    """
    return str

#server /create
@app.route('/create')
def create():
    return "Hi from the create page"


#server /question/<title>
@app.route('/question/<title>')
def question(title):
    return '<h2>' + title + '</h2>' 

