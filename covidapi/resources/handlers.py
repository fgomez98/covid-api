import re
from datetime import date, timedelta
from datetime import datetime

import pandas as pd
from flask_restful import abort

from covidapi.db import query
from covidapi.models.filters import Filters
from covidapi.models.summary import Summary

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


def summary(start_date: date, end_date: date, df: pd.DataFrame):
    current_date = start_date
    summaries = [Summary(current_date)]
    while current_date <= end_date:
        summary = Summary(current_date)
        current_df = query(df, Filters(current_date, current_date))
        casos = current_df.shape[0]
        muertes = query(current_df, Filters(current_date, current_date, dead=True)).shape[0]
        summary.add_casos(casos, summaries[-1].casos_acc + casos)
        summary.add_muertes(muertes, summaries[-1].muertes_acc + muertes)
        summaries.append(summary)
        current_date = current_date + delta
    return summaries[1:]
