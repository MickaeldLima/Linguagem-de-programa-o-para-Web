from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # essa é a primeira tela que vai aparecer (raiz)
def inicio():
    return render_template("inicio.html")

@app.route('/formulario')# segunda página para preenchimento de um formulário
def formulario():
    return render_template("formulario.html")