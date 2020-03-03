from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home')
def home():
    title = 'Atividades Complementares'
    list = ['Oficina de Ads', 'Semana da Matemática']
    return render_template('index.html', titulo=title, eventos = list)
