from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Olá Mundo!"


#http://127.0.0.1:5000 - endereço padrão