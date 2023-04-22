from flask import Flask
from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#o flask group que está dentro do CLI vai cuidar de injetar comandos e executar nossa aplicação 
cli = FlaskGroup(app)

@cli.command()
def create_db(): 
  db.create_all()
  print("Banco de dados criado com sucesso")
  
@cli.command("db_drop")
def db_drop():
    db.drop_all()

@cli.command("db_migrate")
def db_migrate():
    MigrateCommand().run()

from app.controllers import default
