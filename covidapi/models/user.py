from flask_restful_swagger import swagger
from flask_restful import Resource, reqparse, marshal_with, fields

@swagger.model
class User():
    def __init__(self):
        self.age = 25
        self.name = "Juan"

    resource_fields = {
        'name': fields.String,
        'age': fields.Integer
    }