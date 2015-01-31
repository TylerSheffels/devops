from flask import Flask

app = Flask(__name__)
app.config.from_object('apps.settings.settings')
app.config.from_object('apps.settings.localsettings')
# app.config.from_envvar('DEVOPS_SETTINGS')

@app.route('/')
def landing():
    return '{}\nHello {}!'.format(app.config['APPLICATION_NAME'], app.config['USERNAME'])

if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()
