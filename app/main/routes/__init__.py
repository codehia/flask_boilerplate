from .add_todo_restful import TodoSimple
from flask_restful import Api


def add_resources(app):
    api = Api(app)
    api.add_resource(TodoSimple, '/')
