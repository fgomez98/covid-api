from flask_restful import Resource

regions = ['caba', 'buenos aires', 'catamarca', 'córdoba', 'corrientes', 'chaco', 'chubut', 'entre ríos', 'formosa', 'jujuy', 'la pampa', 'la rioja', 'mendoza', 'misiones', 'neuquén', 'río negro', 'salta', 'san juan', 'san luis', 'santa cruz', 'sante fe', 'santiago del estero', 'tucumán', 'tierra del fuego', 'nacional']

class Provinces(Resource):
    def get(self):
        return "Hello"


class Province(Resource):
    def get(self):
        return "Hello"


class ProvinceCount(Resource):

    def get(self):
        return "Hello"
