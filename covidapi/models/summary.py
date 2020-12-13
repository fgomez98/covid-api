from flask_restful import fields

from covidapi.models.summaryhistory import div


class Summary:
    resource_fields = {
        'casos': fields.Integer,
        'muertes': fields.Integer,
        'poblacion': fields.Integer,
        'letalidad': fields.Float,
        'casos_cada_cien_mil': fields.Float,
        'casos_por_millon': fields.Float,
        'muertes_cada_cien_mil': fields.Float,
        'muertes_por_millon': fields.Float
    }

    def __init__(self, population, date=None):
        self.poblacion = population
        self.casos = 0
        self.muertes = 0

    def add_population(self, population):
        self.poblacion = population

    def add_casos_muertes(self, casos, muertes):
        self.casos = casos
        self.muertes = muertes
        self.letalidad = div(muertes, casos)  # todo: en porcentaje o valor entre (0,1) ?
        self.casos_cada_cien_mil = div(casos, self.poblacion) * 100000
        self.casos_por_millon = div(casos, self.poblacion) * 1000000
        self.muertes_cada_cien_mil = div(muertes, self.poblacion) * 100000
        self.muertes_por_millon = div(muertes, self.poblacion) * 1000000
