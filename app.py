from flask import Flask
import boto3
app = Flask(__name__)
rds = boto3.client('rds')


@app.route('/')
def hello_world():
    # try:
    #     dbs = rds.describe_db_instances()
    #     for db in dbs['DSInstances']:
    #         return((%s@%s:s %s) % (db['MasterUsername'], db['Endpoint']['Address'], db['Endpoint']['Port'], db['DBInstanceStatus']))
    # except Exceptions as e:
    #     return e

    return 'Hello, World!hehe change 2 heh jusia kocia lololol. aaa bb c d koszka zzz aIgore'
