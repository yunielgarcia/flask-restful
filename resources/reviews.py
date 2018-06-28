from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse, inputs, fields

import models


class ReviewList(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument(
            'course',
            type=inputs.positive,
            required=True,
            help='No course provided',
            location=['form', 'json']
        )
        self.reqparser.add_argument(
            'rating',
            type=inputs.int_range(1, 5),
            required=True,
            help='No rating provided',
            location=['form', 'json']
        )
        self.reqparser.add_argument(
            'comment',
            type=inputs.int_range(1, 5),
            required=False,
            nullable=True,
            location=['form', 'json'],
            default=''
        )
        super().__init__()

    def get(self):
        return jsonify({'reviews': [
            {
                'course': 1,
                'rating': 5
            }
        ]})


class Review(Resource):
    def get(self):
        return jsonify(
            {
                'course': 1,
                'rating': 5
            }
        )

    def put(self):
        return jsonify(
            {
                'course': 1,
                'rating': 5
            }
        )

    def delete(self):
        return jsonify(
            {
                'course': 1,
                'rating': 5
            }
        )


reviews_api = Blueprint('resources.reviews', __name__)
api = Api(reviews_api)
api.add_resource(
    ReviewList,
    '/reviews',
    endpoint='reviews'
)
api.add_resource(
    Review,
    '/review/<int:id>',
    endpoint='review'
)
