from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

from covidapi.resources.bar import Bar
from covidapi.resources.foo import Foo
from covidapi.resources.national import National, NationalCount
from covidapi.resources.provinces import Provinces, ProvinceCount, Province

app = Flask(__name__)
if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig')

api = swagger.docs(Api(app), apiVersion="0.1", description="My API Swagger doc", )

api.add_resource(Foo, "/foo/<string:user>/")
api.add_resource(Bar, "/bar/")
api.add_resource(National, "/national/")
api.add_resource(NationalCount, "/national/count/")
api.add_resource(Provinces, "/provinces/")
api.add_resource(Province, "/provinces/<string:id>/")
api.add_resource(ProvinceCount, "/provinces/<string:id>/count/")


def run_api(*args, **kwargs):
    app.run(*args, **kwargs)


if __name__ == '__main__':
    run_api()
