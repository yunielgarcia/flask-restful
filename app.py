from flask import Flask

import models
from resources.courses import courses_api
from resources.reviews import reviews_api

DEBUG = True
PORT = 8800
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'da;lfkjadlfdsafasdfjfdaopsifdsaifdoisafakldf=jdaff'
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')

@app.route('/')
def hello_world():
    return 'Hello world'


if __name__ == "__main__":
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
