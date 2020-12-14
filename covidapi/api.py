from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

from covidapi.resources.count import Count
from covidapi.resources.history import History
from covidapi.resources.stats import Stats

app = Flask(__name__)
if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig')

api = swagger.docs(Api(app), apiVersion="0.1", description="Grupo A: API COVID Argentina")

api.add_resource(Stats, "/stats/")
api.add_resource(History, "/historial/")
api.add_resource(Count, "/cantidad/")


def run_api(*args, **kwargs):
    app.run(*args, **kwargs)


if __name__ == '__main__':
    run_api()
