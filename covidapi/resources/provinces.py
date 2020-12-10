from flask_restful import Resource


class Provinces(Resource):
    def get(self):
        return "Hello"


class Province(Resource):
    def get(self):
        return "Hello"


class ProvinceCount(Resource):

    def get(self):
        return "Hello"
