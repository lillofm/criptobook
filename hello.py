from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hola, mundo"


@app.route("/Adios")
def Adios_mundo():
    return "Hasta el jueves"