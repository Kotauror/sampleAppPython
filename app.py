from flask import Flask
from contact import db
from app_config import app
from flask_sqlalchemy import SQLAlchemy
from contacts_book import ContactsBook

contacts_book = ContactsBook()
db.init_app(app)

@app.route('/')
def hello_world():
    numOfCont = contacts_book.get_number_of_contacts()
    contactsString = contacts_book.get_contacts_names_as_string()
    return "There are " + str(numOfCont) + " in the db and the contact names are: " + contactsString
