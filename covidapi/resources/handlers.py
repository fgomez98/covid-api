import re
from datetime import date, timedelta
from datetime import datetime

import pandas as pd
from flask_restful import abort

from covidapi.db import query
from covidapi.models.filters import Filters
from covidapi.models.summary import Summary
from covidapi.population import population_data

delta = timedelta(days=1)


def get_date(value):
    pattern = re.compile("\d{4}-\d{1,2}-\d{1,2}")
    if pattern.match(value):
        return datetime.strptime(value, "%Y-%m-%d").date()
    else:
        raise ValueError("The parameter has to be in the correct format: yyyy-mm-dd")


def get_bool(value):
    if value == 'true':
        return True
    else:
        return False


def raise_general_error():
    abort(404, message="Ups, something went wrong")


def summary(start_date: date, end_date: date, region: str, df: pd.DataFrame):
    population = population_data[region]
    current_date = start_date
    summaries = [Summary(current_date, population)]
    while current_date <= end_date:
        summary = Summary(current_date, population)
        summary.add_population(population)
        filter = Filters()
        filter.add_date(current_date)
        current_df = query(df, filter)
        casos = current_df.shape[0]
        filter.add_dead(True)
        muertes = query(current_df, filter).shape[0]
        summary.add_casos_muertes(casos, summaries[-1].casos_acc + casos, muertes, summaries[-1].muertes_acc + muertes)
        summaries.append(summary)
        current_date = current_date + delta
    return summaries[1:]
