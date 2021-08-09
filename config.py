from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO

import os


caminho = os.path.dirname(os.path.abspath(__file__))    
arquivobd = os.path.join(caminho, "storage.db") 

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+arquivobd 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
