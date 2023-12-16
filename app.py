from flask import Flask
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from tata import deff3
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from db import db
from flask_sqlalchemy import SQLAlchemy
from db.models import users
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = "123"
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(deff3)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)

user_db = 'admin_knowledge_base_orm'
host_ip = '127.0.0.1'
host_port = '5432'
database_name = 'knowledge_base_orm'
password = '123'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password}@{host_ip}:{host_port}/{database_name}'
app.config['SQLALCHEMY_TRACK_NODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()

login_manager.login_view = 'lab6.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(user_id):
    return users.query.get(int(user_id))
