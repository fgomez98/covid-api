import pandas as pd

from config import Config
from covidapi.models.filters import Filters

bool2value = {True: "'SI'", False: "'NO'"}
classification2value = {'confirmed': "'Confirmado'", 'suspected': "'Sospechoso'", 'rejejcted': "'Descartado'"}

# fixme: diferenciar de dev y prod
df = pd.read_csv(Config.DATA_FILE)

def append_to_query(expr, query):
    return expr if query == "" else query + " and " + expr


def query(df, filters: Filters) -> pd.DataFrame:
    # fixme: me enquilombe un poco tratando de que las fechas sean un argumento opcional
    query_build = ""
    if filters.end_date != None and filters.start_date != None:
        query_build = "fecha_apertura >= '" + str(filters.start_date) + "' and " + "fecha_apertura <= '" + str(
        filters.end_date) + "'"
    if filters.dead != None:
        query_build = append_to_query("fallecido == " + bool2value[filters.dead], query_build)
    if filters.icu != None:
        query_build = append_to_query("cuidado_intensivo == " + bool2value[filters.icu], query_build)
    if filters.respirator != None:
        query_build =  append_to_query("asistencia_respiratoria_mecanica == " + bool2value[filters.respirator], query_build)
    if filters.classification != None:
        query_build = append_to_query("clasificacion_resumen == " + classification2value[filters.classification], query_build)
    if query_build != "":
        return df.query(query_build)
    else:
        return df

