import pandas as pd

from config import Config
from covidapi.models.filters import Filters

bool2value = {True: "'SI'", False: "'NO'"}
classification2value = {'confirmed': "'Confirmado'", 'suspected': "'Sospechoso'", 'rejejcted': "'Descartado'"}

# fixme: diferenciar de dev y prod
df = pd.read_csv(Config.DATA_FILE)


def query(df, filters: Filters) -> pd.DataFrame:
    query_build = "fecha_apertura >= '" + str(filters.start_date) + "' and " + "fecha_apertura <= '" + str(
        filters.end_date) + "'"
    if filters.dead != None:
        query_build = query_build + " and fallecido == " + bool2value[filters.dead]
    if filters.icu != None:
        query_build = query_build + " and cuidado_intensivo == " + bool2value[filters.icu]
    if filters.respirator != None:
        query_build = query_build + " and asistencia_respiratoria_mecanica == " + bool2value[filters.respirator]
    if filters.classification != None:
        query_build = query_build + " and clasificacion_resumen == " + classification2value[filters.classification]
    return df.query(query_build)
