from flask import Flask
import time
import os
from models import db
from flask_sqlalchemy import SQLAlchemy
# from models import Contact
from contacts_book import ContactsBook

app = Flask(__name__)
contacts_book = ContactsBook()


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
    contacts = contacts_book.get_contacts()
    return "miaauauuu we have " + str(len(contacts)) + " in the db and the contact names are: " + contacts[0].name + "and " + contacts[1].name + "!"
