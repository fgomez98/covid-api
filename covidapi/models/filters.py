from flask_restful import fields
from flask_restful_swagger import swagger


@swagger.model
class Filters:
    resource_fields = {
        'cui': fields.Boolean,
        'muertos': fields.Boolean,
        'respirador': fields.Boolean,
        'classificacion': fields.String,
        'desde': fields.DateTime,
        'hasta': fields.DateTime,
        'genero': fields.String,
        'min_edad': fields.Integer,
        'anios_meses': fields.String,
        'max_edad': fields.Integer,
        'provincia': fields.String
    }

    def __init__(self):
        self.start_date = None
        self.end_date = None
        self.icu = None
        self.dead = None
        self.respirator = None
        self.classification = None
        self.gender = None
        self.min_age = None
        self.year_month = None
        self.max_age = None
        self.province = None

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

    def add_gender(self, gender):
        self.gender = gender

    def add_age(self, age):
        self.min_age = age
        self.max_age = age

    def add_age_interval(self, min_age, max_age):
        self.min_age = min_age
        self.max_age = max_age

    def add_year_month(self, year_month):
        self.year_month = year_month

    def add_province(self, province):
        self.province = province

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
