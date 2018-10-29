from flask import Flask
import time
import os
from models import db
from flask_sqlalchemy import SQLAlchemy
from models import Contact

# app = Flask(__name__)
# rds = boto3.client('rds', region_name='us-west-1')

# config
# SQLALCHEMY_DATABASE_URI = os.environ.get(
#         'DATABASE_URI', 'postgresql://localhost/contacts')
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

# app.config.from_object(SQLALCHEMY_DATABASE_URI)
# db = SQLAlchemy(app)


# def getNumberOfDBs():
#     try:
#         dbs = rds.describe_db_instances()
#         return len(dbs)
#     except Exception as e:
#         return e

@app.route('/')
def hello_world():
    # numOfDB = getNumberOfDBs()
    # print(numOfDB)
    print("*")
    print(Contact)
    time.sleep(3)
    contacts = Contact.query.all()
    time.sleep(3)
    print("**")
    print(contacts)
    print("***")
    # numOfContacts = len(contacts)
    return "miaauauuu we have " + str(len(contacts)) + " in the db and the contact name is " + contacts[0].name
    # return str(numOfContacts)
    # return "I have " + str(numOfContacts) + "contacts"
    # return "Im using sqlalchemy 2" + "and having probs."
    # return "Hi Mentors! My EC2 instance has: " + str(numOfDB) + " databases, I think it should have one....."
