from datetime import datetime

import pandas as pd

f = pd.ExcelFile('data/c1_proyecciones_prov_2010_2040.xls')
year_index = (datetime.now().year - 2010) + 4

population_data = {}

for sheet_name in f.sheet_names:
    if sheet_name != 'GraphData':
        population_data[sheet_name.split('-')[1].lower()] = f.parse(sheet_name).iloc[year_index, 1]

population_data['nacional'] = population_data.pop('total del país')
population_data['santa fe'] = population_data.pop('sante fe')  ## error lexicografico en el documento
