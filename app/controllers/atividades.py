import os
import uuid

from app import app
from flask import render_template
from app.models.tables import Atividade
from flask import request


# Listando todas as atividades
@app.route('/atividades')
def listar_atividades():
    a = Atividade.query.all()
    for i in range (len(a)):
        a[i].data = a[i].data.strftime('%d/%m/%Y')
    return render_template('atividades_listar.html', atividades = a)

# carregando formulário
@app.route('/atividades/novo')
def form_nova_atividade():
    tipo = 'inserir'
    return render_template("atividades_formulario.html", type= tipo)

# Cadastrar uma nova atividade
@app.route('/atividades/novo', methods = {'POST'})
def inserir_atividade():
    # Recebendo arquivo
    arquivo = request.files['arquivo']
    arquivo.filename = str(uuid.uuid4()) + os.path.splitext(arquivo.filename)[1]
    print(arquivo.filename)
    return ""