from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    frutas = ["Morango", "Uva", "Laranja", "Mamão", "Maçã", "Pêra", "Melão", "Abacaxi"]
    return render_template("index.html", frutas=frutas)

@app.route('/sobre')
def sobre():
    notas = {"Aluno0":5.0, "Aluno1":8.0, "Aluno2":7.0, "Aluno3":8.5}
    return render_template("sobre.html", notas=notas)

#http://127.0.0.1:5000 - endereço padrão