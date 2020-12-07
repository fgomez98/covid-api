from flask_restful import Resource, reqparse, marshal_with
from flask_restful_swagger import swagger

from covidapi.db import query, df
from covidapi.models.filters import Filters
from covidapi.models.summary import Summary
from covidapi.resources.handlers import summary, get_bool, get_date

filters_get_args = reqparse.RequestParser()
filters_get_args.add_argument('icu', type=get_bool, help="filter by cases in icu", required=False)
filters_get_args.add_argument('dead', type=get_bool, help="filter by cases with dead condition", required=False)
filters_get_args.add_argument('respirator', type=get_bool, help="filter by cases with respirator", required=False)
filters_get_args.add_argument('classification', type=str, help="filter by classification", required=False)
filters_get_args.add_argument('from', type=get_date, help="filter from date in format: yyyy-mm-dd", required=True)
filters_get_args.add_argument('to', type=get_date, help="filter to date in format: yyyy-mm-dd", required=True)


class National(Resource):

    @swagger.operation(
        # responseClass=Filters.__name__,
        parameters=[
            {'name': 'icu',
             "required": False,
             'allowMultiple': False,
             'dataType': 'boolean',
             'paramType': 'query'},
            {'name': 'dead',
             "required": False,
             'allowMultiple': False,
             'dataType': 'boolean',
             'paramType': 'query'},
            {'name': 'respirator',
             "required": False,
             'allowMultiple': False,
             'dataType': 'boolean',
             'paramType': 'query'},
            {'name': 'classification',
             "required": False,
             'allowMultiple': False,
             'dataType': 'string',
             'enum': ['confirmed', 'suspected', 'rejejcted'],
             'paramType': 'query'},
            {'name': 'from',
             'description': 'format: yyyy-mm-dd',
             "required": True,
             'allowMultiple': False,
             'dataType': 'datetime',
             'paramType': 'query'},
            {'name': 'to',
             'description': 'format: yyyy-mm-dd',
             "required": True,
             'allowMultiple': False,
             'dataType': 'datetime',
             'paramType': 'query'}
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Ok"
            },
        ]
    )
    @marshal_with(Summary.resource_fields)
    def get(self):
        args = filters_get_args.parse_args()
        filters = Filters(start_date=args.get('from'),
                          end_date=args.get('to'),
                          icu=args.get('icu'),
                          dead=args.get('dead'),
                          respirator=args.get('respirator'),
                          classification=args.get('classification'))
        result = query(df, filters)
        ret = summary(filters.start_date, filters.end_date, result)
        return ret


class NationalCount(Resource):

    @swagger.operation(
        # responseClass=,
        parameters=[
            {'name': 'icu',
             "required": False,
             'allowMultiple': False,
             'dataType': 'boolean',
             'paramType': 'query'},
            {'name': 'dead',
             "required": False,
             'allowMultiple': False,
             'dataType': 'boolean',
             'paramType': 'query'},
            {'name': 'respirator',
             "required": False,
             'allowMultiple': False,
             'dataType': 'boolean',
             'paramType': 'query'},
            {'name': 'classification',
             "required": False,
             'allowMultiple': False,
             'dataType': 'string',
             'enum': ['confirmed', 'suspected', 'rejejcted'],
             'paramType': 'query'},
            {'name': 'from',
             'description': 'format: yyyy-mm-dd',
             "required": True,
             'allowMultiple': False,
             'dataType': 'datetime',
             'paramType': 'query'},
            {'name': 'to',
             'description': 'format: yyyy-mm-dd',
             "required": True,
             'allowMultiple': False,
             'dataType': 'datetime',
             'paramType': 'query'}
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Ok"
            },
        ]
    )
    def get(self):
        args = filters_get_args.parse_args()
        filters = Filters(start_date=args.get('from'),
                          end_date=args.get('to'),
                          icu=args.get('icu'),
                          dead=args.get('dead'),
                          respirator=args.get('respirator'),
                          classification=args.get('classification'))
        return {'count': query(df, filters).shape[0]}
