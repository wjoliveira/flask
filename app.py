from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    fruta1 = "Morango"
    fruta2 = "Uva"
    fruta3 = "Maçã"
    fruta4 = "Laranja"

    return render_template("index.html", fruta1=fruta1, fruta2=fruta2, fruta3=fruta3, fruta4=fruta4)

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

#http://127.0.0.1:5000 - endereço padrão