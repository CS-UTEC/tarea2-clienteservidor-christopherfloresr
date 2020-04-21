from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/espar/<numero>')
def espar(numero):
    return str(int(numero)%2 == 0)

@app.route('/palindrome/<palabra>')
def palindrome(palabra):
    return  str ( palabra  ==  palabra [:: - 1 ])

@app.route('/multiplo/<numero1>/<numero2>')
def multiplo(numero1,numero2):
    return str(int(numero1)%int(numero2) == 0)

@app.route('/static/<content>')#html/hello.hmtl.
def static_content(content):
    return render_template(content)




if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
