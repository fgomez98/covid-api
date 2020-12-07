from flask_restful import fields


class Summary:
    resource_fields = {
        'fecha': fields.String,
        'casos': fields.Integer,
        'casos_acc': fields.Integer,
        'muertes': fields.Integer,
        'muertes_acc': fields.Integer
    }

    def __init__(self, date):
        self.fecha = date
        self.casos = 0
        self.casos_acc = 0
        self.muertes = 0
        self.muertes_acc = 0
        # self.casos_cada_cien_mil 0
        # self.muertes_cada_cien_mil 0
        # self.casos_acum_cada_cien_mil 0
        # self.muertes_acum_cada_cien_mil 0
        # self.casos_por_millón 0
        # self.muertes_por_millón 0
        # self.casos_acum_por_millón 0
        # self.muertes_acum_por_millón 0

    def add_casos(self, casos, casos_acc):
        self.casos = casos
        self.casos_acc = casos_acc

    def add_muertes(self, muertes, muertes_acc):
        self.muertes = muertes
        self.muertes_acc = muertes_acc
