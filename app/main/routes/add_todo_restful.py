from flask import Flask, request
from flask_restful import Resource, Api
from app.main.services.todo_service import add_new_todo


class TodoSimple(Resource):
    def get(self):
        return "Home"

    def post(self):
        data = request.json
        return add_new_todo(data)
