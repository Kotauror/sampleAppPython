from flask import Flask
import time
import os
from models import db
from flask_sqlalchemy import SQLAlchemy
from models import Contact

app = Flask(__name__)

POSTGRES = {
    'user': 'helloNamesAdmin',
    'pw': 'hellonames',
    'db': 'helloNamesAdmin',
    'host': 'hellonames.c9xzd6caea05.us-east-1.rds.amazonaws.com',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def hello_world():
    contacts = Contact.query.all()
    return "miaauauuu we have " + str(len(contacts)) + " in the db and the contact names are: " + contacts[0].name + contacts[1].name
