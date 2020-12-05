from flask import Flask
from flask_restful import Api
from covidapi.resources.foo import Foo
from covidapi.resources.bar import Bar

app = Flask(__name__)
api = Api(app)

api.add_resource(Foo, "/foo/<string:user>")
api.add_resource(Bar, "/bar/")

def run_api(*args, **kwargs):
    app.run(*args, **kwargs)

if __name__ == '__main__':
    run_api()
