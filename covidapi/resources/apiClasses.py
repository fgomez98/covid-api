from datetime import date

from flask_restful import Resource, reqparse, marshal_with
from flask_restful_swagger import swagger

from covidapi.db import query, df
from covidapi.models.filters import Filters
from covidapi.models.summaryhistory import SummaryHistory
from covidapi.models.summary import Summary
from covidapi.resources.handlers import summary, get_bool, get_date, summary_history

regions = ['caba', 'buenos_aires', 'catamarca', 'cordoba', 'corrientes', 'chaco', 'chubut', 'entre_rios', 'formosa',
           'jujuy', 'la_pampa', 'la_rioja', 'mendoza', 'misiones', 'neuquen', 'rio_negro', 'salta', 'san_juan',
           'san_luis', 'santa_cruz', 'sante_fe', 'santiago_del_estero', 'tucuman', 'tierra_del_fuego', 'nacional']

pUtf8 = {'caba': 'caba',
         'buenos_aires': 'buenos aires',
         'catamarca': 'catamarca',
         'cordoba': 'córdoba',
         'corrientes': 'corrientes',
         'chaco': 'chaco',
         'chubut': 'chubut',
         'entre_rios': 'entre ríos',
         'formosa': 'formosa',
         'jujuy': 'jujuy',
         'la_pampa': 'la pampa',
         'la_rioja': 'la rioja',
         'mendoza': 'mendoza',
         'misiones': 'misiones',
         'neuquen': 'neuquén',
         'rio_negro': 'río negro',
         'salta': 'salta',
         'san_juan': 'san juan',
         'san_luis': 'san luis',
         'santa_cruz': 'santa cruz',
         'sante_fe': 'santa fe',
         'santiago_del_estero': 'santiago del estero',
         'tucuman': 'tucumán',
         'tierra_del_fuego': 'tierra del fuego',
         'nacional': 'nacional'}

filters_get_args = reqparse.RequestParser()
filters_get_args.add_argument('cui', type=get_bool, help="filtra por casos en cui", required=False)
filters_get_args.add_argument('muertos', type=get_bool,
                              help="filtra por los casos en que el paciente termino falleciendo", required=False)
filters_get_args.add_argument('respirador', type=get_bool, help="filtra por casos con respirador", required=False)
filters_get_args.add_argument('classificacion', type=str, help="filtra por classificacion", required=False)
filters_get_args.add_argument('desde', type=get_date, help="filtra desde la fecha con el formato: yyyy-mm-dd",
                              required=False)
filters_get_args.add_argument('hasta', type=get_date, help="filtra hasta la fecha con el formato: yyyy-mm-dd",
                              required=False)
filters_get_args.add_argument('sexo', type=str, help="filtra por genero en el formato", required=False)
filters_get_args.add_argument('max_edad', type=int, help="filtra por la edad minima de los infectafos",
                              required=False)
filters_get_args.add_argument('min_edad', type=int, help="filtra por la edad maxima de los infectafos",
                              required=False)
filters_get_args.add_argument('años_meses', type=str, help="filtra si las edades en el filtro estan en años o meses",
                              required=False)
filters_get_args.add_argument('provincia', type=str,
                              help="filtra por provincia, por default usa los valores nacionales", required=False)

parameters = [
    {'name': 'cui',
     "required": False,
     'allowMultiple': False,
     'dataType': 'boolean',
     'paramType': 'query'},
    {'name': 'muertos',
     "required": False,
     'allowMultiple': False,
     'dataType': 'boolean',
     'paramType': 'query'},
    {'name': 'respirador',
     "required": False,
     'allowMultiple': False,
     'dataType': 'boolean',
     'paramType': 'query'},
    {'name': 'classificacion',
     "required": False,
     'allowMultiple': False,
     'dataType': 'string',
     'enum': ['confirmed', 'suspected', 'rejected'],
     'paramType': 'query'},
    {'name': 'desde',
     'description': 'format: yyyy-mm-dd',
     "required": False,
     'allowMultiple': False,
     'dataType': 'datetime',
     'paramType': 'query'},
    {'name': 'hasta',
     'description': 'format: yyyy-mm-dd',
     "required": False,
     'allowMultiple': False,
     'dataType': 'datetime',
     'paramType': 'query'},
    {'name': 'sexo',
     "required": False,
     'allowMultiple': False,
     'dataType': 'string',
     'enum': ['male', 'female'],
     'paramType': 'query'},
    {'name': 'min_edad',
     "required": False,
     'allowMultiple': False,
     'dataType': 'integer',
     'paramType': 'query'
     },
    {'name': 'max_edad',
     "required": False,
     'allowMultiple': False,
     'dataType': 'integer',
     'paramType': 'query'
     },
    {'name': 'anios_meses',
     "required": False,
     'allowMultiple': False,
     'dataType': 'string',
     'enum': ['years', 'months'],
     'paramType': 'query'
     },
    {'name': 'provincia',
     "required": False,
     'allowMultiple': False,
     'dataType': 'string',
     'enum': regions,
     'paramType': 'query'
     }]


class Stats(Resource):
    @swagger.operation(parameters=parameters)
    @marshal_with(Summary.resource_fields)
    def get(self):
        args = filters_get_args.parse_args()
        print(args)
        filters = Filters()
        filters.add_interval(start_date=args.get('desde'), end_date=args.get('hasta'))
        filters.add_icu(icu=args.get('cui'))
        filters.add_dead(dead=args.get('muertos'))
        filters.add_respirator(respirator=args.get('respirador'))
        filters.add_classification(classification=args.get('classificacion'))
        filters.add_gender(args.get('sexo'))
        filters.add_age_interval(args.get('min_edad'), args.get('max_edad'))
        filters.add_year_month(args.get('anios_meses'))
        filters.add_province(province=args.get('provincia'))
        result = query(df, filters)
        p_val = pUtf8[filters.province] if filters.province is not None else pUtf8['nacional']
        if filters.start_date is not None and filters.end_date is not None:
            ret = summary(filters.start_date, filters.end_date, p_val, result)
        else:
            ret = summary(date(year=2020, month=1, day=1), date.today(), p_val, result)
        return ret


class History(Resource):
    @swagger.operation(parameters=parameters)
    @marshal_with(SummaryHistory.resource_fields)
    def get(self):
        args = filters_get_args.parse_args()
        filters = Filters()
        filters.add_interval(start_date=args.get('desde'), end_date=args.get('hasta'))
        filters.add_icu(icu=args.get('cui'))
        filters.add_dead(dead=args.get('muertos'))
        filters.add_respirator(respirator=args.get('respirador'))
        filters.add_classification(classification=args.get('classificacion'))
        filters.add_gender(args.get('sexo'))
        filters.add_age_interval(args.get('min_edad'), args.get('max_edad'))
        filters.add_year_month(args.get('anios_meses'))
        filters.add_province(args.get('provincia'))
        result = query(df, filters)
        p_val = pUtf8[filters.province] if filters.province is not None else pUtf8['nacional']
        if filters.start_date is not None and filters.end_date is not None:
            ret = summary_history(filters.start_date, filters.end_date, p_val, result)
        else:
            ret = summary_history(date(year=2020, month=1, day=1), date.today(), p_val, result)
        return ret


class Count(Resource):
    @swagger.operation(parameters=parameters)
    def get(self):
        args = filters_get_args.parse_args()
        filters = Filters()
        filters.add_interval(start_date=args.get('desde'), end_date=args.get('hasta'))
        filters.add_icu(icu=args.get('cui'))
        filters.add_dead(dead=args.get('muertos'))
        filters.add_respirator(respirator=args.get('respirador'))
        filters.add_classification(classification=args.get('classificacion'))
        filters.add_gender(args.get('sexo'))
        filters.add_age_interval(args.get('min_edad'), args.get('max_edad'))
        filters.add_year_month(args.get('anios_meses'))
        filters.add_province(args.get('provincia'))
        return {'cantidad': query(df, filters).shape[0]}
