from datetime import date

from flask_restful import Resource, marshal_with
from flask_restful_swagger import swagger

from covidapi.db import query, df
from covidapi.models.filters import Filters
from covidapi.models.stats import Stats
from covidapi.resources.resource_handlers import summary
from covidapi.resources.resource_utils import parameters, filters_get_args, pUtf8


class Stats(Resource):
    @swagger.operation(responseClass=Stats.__name__, parameters=parameters)
    @marshal_with(Stats.resource_fields)
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
        filters.add_province(province=args.get('region'))
        result = query(df, filters)
        p_val = pUtf8[filters.province] if filters.province is not None else pUtf8['nacional']
        if filters.start_date is not None and filters.end_date is not None:
            ret = summary(filters.start_date, filters.end_date, p_val, result)
        else:
            ret = summary(date(year=2020, month=1, day=1), date.today(), p_val, result)
        return ret
