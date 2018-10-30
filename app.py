from flask import Flask
from contact import db
from app_config import app
from flask_sqlalchemy import SQLAlchemy
from contacts_book import ContactsBook

contacts_book = ContactsBook()
db.init_app(app)

@app.route('/')
def hello_world():
    contacts = contacts_book.get_contacts()
    return "miaauauuu we have " + str(len(contacts)) + " in the db and the contact names are: " + contacts[0].name + " and " + contacts[1].name + "!!"
