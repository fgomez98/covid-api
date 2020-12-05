from covidapi.models.user import User
from flask_restful import Resource, reqparse, marshal_with, fields

bar_get_args = reqparse.RequestParser()
bar_get_args.add_argument('name', type=str, help="Input a name for Bar", required=True)
bar_get_args.add_argument('age', type=int, help="Input age for Bar", required=True)

user_fields = {
    'name': fields.String,
    'age': fields.Integer
}

class Bar(Resource):
    def get(self):
        args = bar_get_args.parse_args()
        return args.copy() # devuelve el mismo diccionario

    @marshal_with(user_fields)
    def post(self):
        juan = User()
        return juan
