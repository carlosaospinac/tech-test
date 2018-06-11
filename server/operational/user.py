from http import HTTPStatus

from sanic.views import HTTPMethodView
from sanic.response import json

from .base_view import BaseView

class User(BaseView):

    def __init__(self):
        super().__init__()
        self.collection = self.database.users

    def post(self, request, arg=None):
        return self.response_status(501)

    def get(self, request, id=None):
        if not id:
            return self.response_status(
                200, self.collection.find()
            )
        print(self.collection.find_one({'_id': id}))
        # return self.response_status(404)
        return self.response_status(
            200, self.collection.find_one({'_id': id})
        )

    def put(self, request, arg=None):
        return self.response_status(501)

    def patch(self, request, arg=None):
        return self.response_status(501)

    def delete(self, request, arg=None):
        return self.response_status(501)