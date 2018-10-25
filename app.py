from flask import Flask
# import boto3
app = Flask(__name__)
# rds = boto3.client('rds', region_name='us-west-1')


@app.route('/')
def hello_world():
    # try:
    #     dbs = rds.describe_db_instances()
    #     length = len(dbs)
    #     return length
    #     for db in dbs['DSInstances']:
    #         return((%s@%s:s %s) % (db['MasterUsername'], db['Endpoint']['Address'], db['Endpoint']['Port'], db['DBInstanceStatus']))
    # except Exceptions as e:
    #     return e

    return 'Hello, World!hehe change 2 heh jusia kocia lololol. aaa bb c d koszka zzz aIgore kotore'
