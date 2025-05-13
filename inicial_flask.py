from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>INDEX Page!</p>"

@app.route('/hello')
def hello():
    return "<p>Hello World Page!</p>"

@app.route('/mateuspa')
def mateuspa():
    return render_template('mateuspa.html')

def main():
    nome = input("Digite seu nome: ")
    print(f"Olá {nome}, seja bem-vindo ao Flask!")

main()