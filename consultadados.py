from flask import Flask, render_template, request
import pandas as pd
import sqlite3
import os
import logging

logging.basicConfig()

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(dir_path, 'dados.db')

def get_data():
   with open('projetointegrador_cliente.sql') as f:
    sql_script = f.read()
    conn = sqlite3.connect(':memory:')
    conn.executescript(sql_script)

    c = conn.cursor()

    # Substitui caracteres nulos por uma string vazia
    sql = """
        SELECT nome, documento, email, endereco
        FROM projetointegrador_cliente
        """.replace('\x00', '')
    
    c.execute(sql)
    results = c.fetchall()
    data = pd.DataFrame(results, columns=['Nome', 'Documento', 'Email', 'Endereço'])

    conn.close()

    return data



@app.route('/', methods=['GET', 'POST'])
def table():
    if request.method == 'POST':
        # Obter os dados do formulário
        nome = request.form.get('nome')
        documento = request.form.get('documento')
        email = request.form.get('email')
        endereco = request.form.get('endereco')
        
        # Inserir os dados no banco de dados
        conn = sqlite3.connect('dados.db')
        c = conn.cursor()
        c.execute("INSERT INTO pessoas (nome, documento, email, endereco) VALUES (?, ?, ?, ?)", (nome, documento, email, endereco))
        conn.commit()
        conn.close()
    
    data = get_data()
    df = pd.DataFrame(data, columns=['Nome', 'Documento', 'Email', 'Endereço'])
    return render_template('table.html', data=df.to_html())


if __name__ == '__main__':
    app.run(port=5000)







