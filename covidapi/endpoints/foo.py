from flask_restful import Resource
from covidapi.endpoints.handlers import raise_general_error

class Foo(Resource):
    def get(self, user):
        return {'msg': 'Hello ' + user + ' i am Foo'}, 200 # <= asi se agrega un codigo de retorno

    def post(self, user):
        return {'msg': 'Bye Foo'}, 200

    def delete(self, user):
        raise_general_error()