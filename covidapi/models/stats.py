from flask_restful import fields
from flask_restful_swagger import swagger

#    Safe zero division method
def div(a, b):
    return round(a / b, 5) if b != 0 else 0

@swagger.model
class Stats():
    # variable de clase para flask
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

    def __init__(self, population):
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


@swagger.model
class StatsHistory(Stats):
    # variable de clase para flask
    resource_fields = {
        ### Summary History
        'fecha': fields.String,
        ### Summary
        'casos': fields.Integer,
        'muertes': fields.Integer,
        ### Summary History
        'casos_acc': fields.Integer,
        'muertes_acc': fields.Integer,
        ### Summary
        'poblacion': fields.Integer,
        'letalidad': fields.Float,
        'casos_cada_cien_mil': fields.Float,
        'casos_por_millon': fields.Float,
        'muertes_cada_cien_mil': fields.Float,
        'muertes_por_millon': fields.Float,
        ### Summary History
        'casos_acc_cada_cien_mil': fields.Float,
        'casos_acc_por_millon': fields.Float,
        'muertes_acc_cada_cien_mil': fields.Float,
        'muertes_acc_por_millon': fields.Float
    }

    def __init__(self, population, date):
        super().__init__(population)
        self.fecha = date
        self.casos_acc = 0
        self.muertes_acc = 0

    def add_casos_muertes_acc(self, casos, casos_acc, muertes, muertes_acc):
        super().add_casos_muertes(casos, muertes)
        self.casos_acc = casos_acc
        self.muertes_acc = muertes_acc
        self.casos_acc_cada_cien_mil = div(casos_acc, self.poblacion) * 100000
        self.casos_acc_por_millon = div(casos_acc, self.poblacion) * 1000000
        self.muertes_acc_cada_cien_mil = div(muertes_acc, self.poblacion) * 100000
        self.muertes_acc_por_millon = div(muertes_acc, self.poblacion) * 1000000
