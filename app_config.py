from flask import Flask

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
