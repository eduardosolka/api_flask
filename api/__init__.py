from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pyodbc

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('config') #pega as configuracoes do arquivo config
db.init_app(app)

migrate = Migrate(app, db)
api = Api(app)

from .views import curso_views

