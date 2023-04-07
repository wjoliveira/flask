from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    frutas = ["Morango", "Uva", "Maçã", "Laranja"]
    return render_template("index.html", frutas=frutas)

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

#http://127.0.0.1:5000 - endereço padrão