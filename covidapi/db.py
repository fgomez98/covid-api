import pandas as pd

from config import Config
from covidapi.models.filters import Filters

bool2value = {True: "'SI'", False: "'NO'"}
classification2value = {'confirmed': "'Confirmado'", 'suspected': "'Sospechoso'", 'rejected': "'Descartado'"}
age = {'years': "'Años'", 'months': "'Meses'"}
gender = {'male': "'M'", 'female': "'F'"}
regions = {'caba': "'CABA'",
           'buenos_aires': "'Buenos Aires'",
           'catamarca': "'Catamarca'",
           'cordoba': "'Córdoba'",
           'corrientes': "'Corrientes'",
           'chaco': "'Chaco'",
           'chubut': "'Chubut'",
           'entre_rios': "'Entre Ríos'",
           'formosa': "'Formosa'",
           'jujuy': "'Jujuy'",
           'la_pampa': "'La Pampa'",
           'la_rioja': "'La Rioja'",
           'mendoza': "'Mendoza'",
           'misiones': "'Misiones'",
           'neuquen': "'Neuquén'",
           'rio_negro': "'Río Negro'",
           'salta': "'Salta'",
           'san_juan': "'San Juan'",
           'san_luis': "'San Luis'",
           'santa_cruz': "'Santa Cruz'",
           'sante_fe': "'Santa Fe'",
           'santiago_del_estero': "'Santiago del Estero'",
           'tucuman': "'Tucumán'",
           'tierra_del_fuego': "'Tierra del Fuego'",
           }


# fixme: diferenciar de dev y prod
df = pd.read_csv(Config.DATA_FILE)


def append_to_query(expr, query):
    return expr if query == "" else query + " and " + expr


def query(data_frame, filters: Filters) -> pd.DataFrame:
    # fixme: me enquilombe un poco tratando de que las fechas sean un argumento opcional
    query_build = ""
    if filters.end_date is not None and filters.start_date is not None:
        query_build = "fecha_apertura >= '" + str(filters.start_date) + "' and " + "fecha_apertura <= '" + str(
            filters.end_date) + "'"
    if filters.dead is not None:
        query_build = append_to_query("fallecido == " + bool2value[filters.dead], query_build)
    if filters.icu is not None:
        query_build = append_to_query("cuidado_intensivo == " + bool2value[filters.icu], query_build)
    if filters.respirator is not None:
        query_build = append_to_query("asistencia_respiratoria_mecanica == " + bool2value[filters.respirator],
                                      query_build)
    if filters.classification is not None:
        query_build = append_to_query("clasificacion_resumen == " + classification2value[filters.classification],
                                      query_build)
    if filters.gender is not None:
        query_build = append_to_query("sexo == " + gender[filters.gender], query_build)

    age_month = classification2value[filters.year_month] if filters.year_month is not None else "'Años'"
    age_flag = False

    if filters.min_age is not None:
        age_flag = True
        query_build = append_to_query("edad >= " + str(filters.min_age), query_build)

    if filters.max_age is not None:
        age_flag = True
        max_age_str = "edad <= " + str(filters.max_age)
        if age_month != 'Meses' and filters.min_age is None:
            max_age_str = '(' + max_age_str + " or edad_años_meses == 'Meses')"
            age_flag = False
        query_build = append_to_query(max_age_str, query_build)

    if age_flag:
        query_build = append_to_query("edad_años_meses == " + age_month, query_build)

    if filters.province is not None and filters.province != 'nacional':
        query_build = append_to_query("residencia_provincia_nombre == " + regions[filters.province], query_build)

    if query_build != "":
        return data_frame.query(query_build)
    else:
        return data_frame
