from flask import Flask, request
from apps.mathengine.engine import handleRequest
import json

app = Flask(__name__)
app.config.from_object('apps.settings.settings')
app.config.from_object('apps.settings.localsettings')
# app.config.from_envvar('DEVOPS_SETTINGS')

@app.route('/', methods=['POST'])
def landing():
    # This is going to be funky, but things need to work now.
    for operation in request.form.keys():
        print operation
        json_operation = json.loads(operation)
        response = handleRequest(json_operation)
    return "Application Name: {} \n{}".format(app.config['APPLICATION_NAME'], response)

if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()
