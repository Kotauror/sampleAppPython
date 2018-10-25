from flask import Flask
import boto3
app = Flask(__name__)
rds = boto3.client('rds', region_name='us-west-1')

def getNumberOfDBs():
    try:
        dbs = rds.describe_db_instances()
        return len(dbs)
    except Exception as e:
        return e

@app.route('/')
def hello_world():
    numOfDB = getNumberOfDBs()
    print(numOfDB)
    return "Hi Mentors! My EC2 instance has: " + str(numOfDB) + " databases, how cool is that. Test"
