from contextlib import closing
from flask import Flask, request
from apps.mathengine.engine import handleRequest
import json
import sqlite3

app = Flask(__name__)
app.config.from_object('apps.settings.settings')
app.config.from_object('apps.settings.localsettings')
# app.config.from_envvar('DEVOPS_SETTINGS')

def log_operation(operation):
    with closing(connect_db()) as db:
        cur = db.cursor()
        insert = "INSERT INTO logging VALUES (NULL, '%s')" % operation
        cur.execute(insert)
        result = cur.execute("select * from logging")
        for row in result:
            print row


@app.route('/', methods=['POST'])
def landing():
    # This is going to be funky, but things need to work now.
    for operation in request.form.keys():
        log_operation(operation)
        json_operation = json.loads(operation)
        response = handleRequest(json_operation)
    return "Application Name: {} \n{}".format(app.config['APPLICATION_NAME'], response)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('apps/database/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        print 'Database Initialized'

if __name__ == '__main__':
    init_db()
    app.debug = app.config['DEBUG']
    app.run()
