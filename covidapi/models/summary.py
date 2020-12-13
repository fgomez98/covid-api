from flask_restful import fields


#    Safe zero division method
def div(a, b):
    return round(a / b, 4) if b != 0 else 0


class Summary:
    resource_fields = {
        'fecha': fields.String,
        'casos': fields.Integer,
        'casos_acc': fields.Integer,
        'muertes': fields.Integer,
        'muertes_acc': fields.Integer,
        'poblacion': fields.Integer,
        'letalidad': fields.Float,
        'casos_cada_cien_mil': fields.Float,
        'casos_por_millon': fields.Float,
        'muertes_cada_cien_mil': fields.Float,
        'muertes_por_millon': fields.Float,
        'casos_acc_cada_cien_mil': fields.Float,
        'casos_acc_por_millon': fields.Float,
        'muertes_acc_cada_cien_mil': fields.Float,
        'muertes_acc_por_millon': fields.Float
    }

    def __init__(self, population, date=None):
        self.fecha = date
        self.poblacion = population
        self.casos = 0
        self.casos_acc = 0
        self.muertes = 0
        self.muertes_acc = 0

    def add_population(self, population):
        self.poblacion = population

    def add_casos_muertes_acc(self, casos, casos_acc, muertes, muertes_acc):
        self.casos = casos
        self.casos_acc = casos_acc
        self.muertes = muertes
        self.muertes_acc = muertes_acc
        self.letalidad = div(muertes, casos)  # todo: en porcentaje o valor entre (0,1) ?
        self.casos_cada_cien_mil = div(casos, self.poblacion) * 100000
        self.casos_por_millon = div(casos, self.poblacion) * 1000000
        self.muertes_cada_cien_mil = div(muertes, self.poblacion) * 100000
        self.muertes_por_millon = div(muertes, self.poblacion) * 1000000
        self.casos_acc_cada_cien_mil = div(casos_acc, self.poblacion) * 100000
        self.casos_acc_por_millon = div(casos_acc, self.poblacion) * 1000000
        self.muertes_acc_cada_cien_mil = div(muertes_acc, self.poblacion) * 100000
        self.muertes_acc_por_millon = div(muertes_acc, self.poblacion) * 1000000

    def add_casos_muertes(self, casos, muertes):
        self.casos = casos
        self.muertes = muertes
        self.letalidad = div(muertes, casos)  # todo: en porcentaje o valor entre (0,1) ?
        self.casos_cada_cien_mil = div(casos, self.poblacion) * 100000
        self.casos_por_millon = div(casos, self.poblacion) * 1000000
        self.muertes_cada_cien_mil = div(muertes, self.poblacion) * 100000
        self.muertes_por_millon = div(muertes, self.poblacion) * 1000000
