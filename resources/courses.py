from flask import jsonify
from flask.ext.restful import Resource

import models


class CourseList(Resource):
    def get(self):
        return jsonify({'courses': [
            {
                'title': 'python basics',

            }
        ]})


class Course(Resource):
    def get(self):
        return jsonify(
            {
                'title': 'python basics',
            }
        )

    def put(self):
        return jsonify(
            {
                'title': 'python basics',
            }
        )

    def delete(self):
        return jsonify(
            {
                'title': 'python basics',
            }
        )