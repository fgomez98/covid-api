from flask_restful import fields
from flask_restful_swagger import swagger
from datetime import date

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

    def __init__(self):
        self.start_date = None
        self.end_date = None
        self.icu = None
        self.dead = None
        self.respirator = None
        self.classification = None

    def add_date(self, date):
        self.start_date = date
        self.end_date = date

    def add_interval(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def add_icu(self, icu):
        self.icu = icu

    def add_dead(self, dead):
        self.dead = dead

    def add_respirator(self, respirator):
        self.respirator = respirator

    def add_classification(self, classification):
        self.classification = classification
