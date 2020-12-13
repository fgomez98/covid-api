from flask_restful import reqparse

from covidapi.resources.resource_handlers import get_bool, get_date

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
filters_get_args.add_argument('classificacion', choices=['confirmed', 'suspected', 'rejected'],
                              help="El valor indicado no es valido, posibles: 'confirmed', 'suspected', 'rejected'",
                              required=False)
filters_get_args.add_argument('desde', type=get_date, help="filtra desde la fecha con el formato: yyyy-mm-dd",
                              required=False)
filters_get_args.add_argument('hasta', type=get_date, help="filtra hasta la fecha con el formato: yyyy-mm-dd",
                              required=False)
filters_get_args.add_argument('sexo', choices=['male', 'female'],
                              help="El valor indicado no es valido, posibles: 'male', 'female'", required=False)
filters_get_args.add_argument('max_edad', type=int, help="filtra por la edad minima de los infectafos",
                              required=False)
filters_get_args.add_argument('min_edad', type=int, help="filtra por la edad maxima de los infectafos",
                              required=False)
filters_get_args.add_argument('años_meses', choices=['years', 'months'],
                              help="El valor indicado no es valido, posibles: 'years', 'months'",
                              required=False)
filters_get_args.add_argument('region', choices=regions,
                              help="La region indicada no es valida", required=False)

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
    {'name': 'region',
     "required": False,
     'allowMultiple': False,
     'dataType': 'string',
     'enum': regions,
     'paramType': 'query'
     }]
