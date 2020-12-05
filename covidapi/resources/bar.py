from flask_restful_swagger import swagger
from covidapi.models.user import User
from flask_restful import Resource, reqparse, marshal_with, fields

bar_get_args = reqparse.RequestParser()
bar_get_args.add_argument('name', type=str, help="Input a name for Bar", required=True)
bar_get_args.add_argument('age', type=int, help="Input age for Bar", required=True)

class Bar(Resource):

    @swagger.operation(
        responseClass=User.__name__,
        parameters=[
            {'name': 'name',
             'description': 'User name',
             "required": True,
             'allowMultiple': False,
             'dataType': 'string',
             'paramType': 'query'},
            {'name': 'age',
             'description': 'User age',
             "required": True,
             'allowMultiple': False,
             'dataType': 'int',
             'paramType': 'query'},
            # {
            #     "name": "name",
            #     "description": "User input",
            #     "required": True,
            #     "allowMultiple": False,
            #     "dataType": User.__name__,
            #     "paramType": "body"
            # }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Todo ok"
            },
        ]
    )
    def get(self):
        args = bar_get_args.parse_args()
        return args.copy() # devuelve el mismo diccionario


    '''
        Takes raw data (in the form of a dict, list, object) and a dict of fields
        to output and filters the data based on those fields.
    '''
    @marshal_with(User.resource_fields)
    @swagger.operation(
        responseClass=User.__name__,
        responseMessages=[
            {
                "code": 200,
                "message": "Todo ok"
            },
        ]
    )
    def post(self):
        juan = User()
        return juan
