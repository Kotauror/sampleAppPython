from flask import Flask
import boto3
import os
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# rds = boto3.client('rds', region_name='us-west-1')

// config
# SQLALCHEMY_DATABASE_URI = os.environ.get(
#         'DATABASE_URI', 'postgresql://localhost/contacts')

app = Flask(__name__)
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
    return "Im using sqlalchemy"
    # return "Hi Mentors! My EC2 instance has: " + str(numOfDB) + " databases, I think it should have one....."
