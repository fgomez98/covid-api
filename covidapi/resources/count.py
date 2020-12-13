from flask_restful import Resource
from flask_restful_swagger import swagger

from covidapi.db import query, df
from covidapi.models.filters import Filters
from covidapi.resources.resource_utils import parameters, filters_get_args


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
        filters.add_province(args.get('region'))
        return {'cantidad': query(df, filters).shape[0]}
