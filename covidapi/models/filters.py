from datetime import date

from flask_restful import fields
from flask_restful_swagger import swagger


@swagger.model
class Filters:
    resource_fields = {
        'icu': fields.Boolean,
        'dead': fields.Boolean,
        'respirator': fields.Boolean,
        'classification': fields.String,
        'from': fields.DateTime,
        'to': fields.DateTime
    }

    def __init__(self, start_date: date,
                 end_date: date,
                 icu: bool = None,
                 dead: bool = None,
                 respirator: bool = None,
                 classification: str = None):
        self.start_date = start_date
        self.end_date = end_date
        self.icu = icu
        self.dead = dead
        self.respirator = respirator
        self.classification = classification
