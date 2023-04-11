from flask import Flask, render_template, request, redirect, flash
import urllib.request, json
from flask_sqlalchemy import SQLAlchemy
import pymysql

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# configure the SQLite database, relative to the app instance folder
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.sqlite3"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://geek:university@localhost:3306/db_cursos"

# initialize the app with the extension
db.init_app(app)

frutas = []
registros = []

class Cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    ch = db.Column(db.Integer)

    def __init__(self, nome, descricao, ch):
        self.nome = nome
        self.descricao = descricao
        self.ch = ch


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas)

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
    return render_template("sobre.html", registros=registros)

@app.route('/filmes/<propriedade>')
def filmes(propriedade):

    if propriedade == "populares":
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=ea18c9592befcd0f9e9edd821813cbb6"
    elif propriedade == "kids":
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=ea18c9592befcd0f9e9edd821813cbb6"
    elif propriedade == "2010":
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=ea18c9592befcd0f9e9edd821813cbb6"
    elif propriedade == "drama":
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=ea18c9592befcd0f9e9edd821813cbb6"
    elif propriedade == "tom_cruise":
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=ea18c9592befcd0f9e9edd821813cbb6"
    else:
        return render_template("page_not_found.html")
    
    resposta = urllib.request.urlopen(url)

    dados = resposta.read()

    jsondata = json.loads(dados)

    return render_template("filmes.html", filmes=jsondata['results'])

@app.route('/cursos')
def lista_cursos():
    return render_template("cursos.html", cursos=Cursos.query.all())

@app.route('/criar_curso', methods=["GET", "POST"])
def criar_curso():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    ch = request.form.get("ch")

    if request.method == "POST":
        if not nome or not descricao or not ch:
            flash("Preencha todos os campos do formulário!","error")
        else:
            curso = Cursos(nome, descricao, ch)
            db.session.add(curso)
            db.session.commit()
            return redirect("/cursos")
    return render_template("novo_curso.html")

@app.route('/atualizar_curso/<int:id>', methods=["GET", "POST"])
def atualizar_curso(id):
    curso = Cursos.query.filter_by(id=id).first()



    return render_template("atualizar_curso.html", curso=curso)
    

if __name__=="__main__":
    db.create_all()
    #app.run(debug=True)

#http://127.0.0.1:5000 - endereço padrão