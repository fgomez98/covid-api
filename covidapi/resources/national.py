from datetime import date

from flask_restful import Resource, reqparse, marshal_with
from flask_restful_swagger import swagger

from covidapi.db import query, df
from covidapi.models.filters import Filters
from covidapi.models.summaryhistory import SummaryHistory
from covidapi.resources.handlers import summary, get_bool, get_date, summary_history

filters_get_args = reqparse.RequestParser()
filters_get_args.add_argument('icu', type=get_bool, help="filter by cases in icu", required=False)
filters_get_args.add_argument('dead', type=get_bool, help="filter by cases with dead condition", required=False)
filters_get_args.add_argument('respirator', type=get_bool, help="filter by cases with respirator", required=False)
filters_get_args.add_argument('classification', type=str, help="filter by classification", required=False)
filters_get_args.add_argument('from', type=get_date, help="filter from date in format: yyyy-mm-dd", required=False)
filters_get_args.add_argument('to', type=get_date, help="filter to date in format: yyyy-mm-dd", required=False)


class National(Resource):
    @swagger.operation(
        # responseClass=Summary.__name__,
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
             'enum': ['confirmed', 'suspected', 'rejected'],
             'paramType': 'query'},
            {'name': 'from',
             'description': 'format: yyyy-mm-dd',
             "required": False,
             'allowMultiple': False,
             'dataType': 'datetime',
             'paramType': 'query'},
            {'name': 'to',
             'description': 'format: yyyy-mm-dd',
             "required": False,
             'allowMultiple': False,
             'dataType': 'datetime',
             'paramType': 'query'}
        ]
    )
    @marshal_with(SummaryHistory.resource_fields)
    # fixme: me enquilombe un poco tratando de que las fechas sean un argumento opcional
    def get(self):
        args = filters_get_args.parse_args()
        filters = Filters()
        filters.add_interval(start_date=args.get('from'), end_date=args.get('to'))
        filters.add_icu(icu=args.get('icu'))
        filters.add_dead(dead=args.get('dead'))
        filters.add_respirator(respirator=args.get('respirator'))
        filters.add_classification(classification=args.get('classification'))
        result = query(df, filters)
        if filters.start_date is not None and filters.end_date is not None:
            ret = summary(filters.start_date, filters.end_date, 'nacional', result)
        else:
            ret = summary(date(year=2020, month=1, day=1), date.today(), 'nacional', result)
        return ret


class NationalHistory(Resource):

    @swagger.operation(
        # responseClass=Summary.__name__,
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
             'enum': ['confirmed', 'suspected', 'rejected'],
             'paramType': 'query'},
            {'name': 'from',
             'description': 'format: yyyy-mm-dd',
             "required": False,
             'allowMultiple': False,
             'dataType': 'datetime',
             'paramType': 'query'},
            {'name': 'to',
             'description': 'format: yyyy-mm-dd',
             "required": False,
             'allowMultiple': False,
             'dataType': 'datetime',
             'paramType': 'query'}
        ]
    )
    @marshal_with(SummaryHistory.resource_fields)
    # fixme: me enquilombe un poco tratando de que las fechas sean un argumento opcional
    def get(self):
        args = filters_get_args.parse_args()
        filters = Filters()
        filters.add_interval(start_date=args.get('from'), end_date=args.get('to'))
        filters.add_icu(icu=args.get('icu'))
        filters.add_dead(dead=args.get('dead'))
        filters.add_respirator(respirator=args.get('respirator'))
        filters.add_classification(classification=args.get('classification'))
        result = query(df, filters)
        if filters.start_date is not None and filters.end_date is not None:
            ret = summary_history(filters.start_date, filters.end_date, 'nacional', result)
        else:
            ret = summary_history(date(year=2020, month=1, day=1), date.today(), 'nacional', result)
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
             'enum': ['confirmed', 'suspected', 'rejected'],
             'paramType': 'query'},
            {'name': 'from',
             'description': 'format: yyyy-mm-dd',
             "required": False,
             'allowMultiple': False,
             'dataType': 'datetime',
             'paramType': 'query'},
            {'name': 'to',
             'description': 'format: yyyy-mm-dd',
             "required": False,
             'allowMultiple': False,
             'dataType': 'datetime',
             'paramType': 'query'}
        ]
    )
    def get(self):
        args = filters_get_args.parse_args()
        filters = Filters()
        filters.add_interval(start_date=args.get('from'), end_date=args.get('to'))
        filters.add_icu(icu=args.get('icu'))
        filters.add_dead(dead=args.get('dead'))
        filters.add_respirator(respirator=args.get('respirator'))
        filters.add_classification(classification=args.get('classification'))
        return {'count': query(df, filters).shape[0]}
