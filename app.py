from flask import Flask

import models

DEBUG = True
PORT = 8800
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'da;lfkjadlfdsafasdfjfdaopsifdsaifdoisafakldf=jdaff'


@app.route('/')
def hello_world():
    return 'Hello world'


if __name__ == "__main__":
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
