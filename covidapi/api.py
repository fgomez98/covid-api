from flask import Flask
from flask_restful import Api
from covidapi.resources.foo import Foo
from covidapi.resources.bar import Bar
from flask_restful_swagger import swagger


app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion="0.1",
    description="My API Swagger doc",)

api.add_resource(Foo, "/foo/<string:user>/")
api.add_resource(Bar, "/bar/")

def run_api(*args, **kwargs):
    app.run(*args, **kwargs)

if __name__ == '__main__':
    run_api()
