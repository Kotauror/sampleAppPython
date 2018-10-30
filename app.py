from flask import Flask, render_template
from contact import db
from app_config import app
from flask_sqlalchemy import SQLAlchemy
from contacts_book import ContactsBook

contacts_book = ContactsBook()
db.init_app(app)

@app.route('/')
def hello_world():
    contacts = contacts_book.get_contacts()
    number_of_contacts = contacts_book.get_number_of_contacts()
    return render_template('index.html', number_of_contacts = number_of_contacts, contacts = contacts)
