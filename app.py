from flask import Flask
import boto3
import os
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# rds = boto3.client('rds', region_name='us-west-1')

# config
# SQLALCHEMY_DATABASE_URI = os.environ.get(
#         'DATABASE_URI', 'postgresql://localhost/contacts')

POSTGRES = {
    'user': 'helloNamesAdmin',
    'pw': 'hellonames',
    'db': 'helloNamesAdmin',
    'host': 'hellonames.c9xzd6caea05.us-east-1.rds.amazonaws.com',
    'port': '5432',
}
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

# app.config.from_object(SQLALCHEMY_DATABASE_URI)
db = SQLAlchemy(app)


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
    return "Im using sqlalchemy 2" + "and having probs."
    # return "Hi Mentors! My EC2 instance has: " + str(numOfDB) + " databases, I think it should have one....."
