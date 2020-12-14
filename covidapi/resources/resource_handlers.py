import re
from datetime import date, timedelta
from datetime import datetime

import pandas as pd
from flask_restful import abort

from covidapi.db import query
from covidapi.models.filters import Filters
from covidapi.models.stats import StatsHistorial, Stats
from covidapi.population import population_data

delta = timedelta(days=1)


def get_date(value):
    pattern = re.compile("\d{4}-\d{1,2}-\d{1,2}")
    if pattern.match(value):
        return datetime.strptime(value, "%Y-%m-%d").date()
    else:
        raise ValueError("El parametro tiene que estar con el formato adecuado: yyyy-mm-dd")


def get_bool(value: str):
    if value.lower() == 'true':
        return True
    else:
        return False


def raise_general_error():
    abort(404, message="Ups, Hubo un error con algo, impresionante")


def summary(start_date: date, end_date: date, region: str, df: pd.DataFrame):
    population = population_data[region]
    summary = Stats(population=population)
    filter = Filters()
    filter.add_interval(start_date, end_date)
    current_df = query(df, filter)
    casos = current_df.shape[0]
    filter.add_dead(True)
    muertes = query(current_df, filter).shape[0]
    summary.add_casos_muertes(casos, muertes)
    return summary


def summary_history(start_date: date, end_date: date, region: str, df: pd.DataFrame):
    population = population_data[region]
    current_date = start_date
    summaries = [StatsHistorial(date=current_date, population=population)]
    while current_date <= end_date:
        summary = StatsHistorial(date=current_date, population=population)
        summary.add_population(population)
        filter = Filters()
        filter.add_date(current_date)
        current_df = query(df, filter)
        casos = current_df.shape[0]
        filter.add_dead(True)
        muertes = query(current_df, filter).shape[0]
        summary.add_casos_muertes_acc(casos, summaries[-1].casos_acc + casos, muertes,
                                      summaries[-1].muertes_acc + muertes)
        summaries.append(summary)
        current_date = current_date + delta
    return summaries[1:]
