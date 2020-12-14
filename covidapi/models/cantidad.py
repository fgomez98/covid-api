from flask_restful import fields
from flask_restful_swagger import swagger


@swagger.model
class Cantidad():

    resource_fields = {
        'cantidad': fields.Integer
    }

    def __init__(self, cantidad):
        self.cantidad = cantidad
