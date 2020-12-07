# from flask_sqlalchemy import SQLAlchemy
# from covidapi.api import app

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/
# modelo para bd, si es que llegamos a usar

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<nombre_usuario>:<password>@<host>:<puerto>/<nombre_basededatos>'
# db = SQLAlchemy(app)

# class Case(db.Model):
#     id_evento_caso = db.Column(db.Integer, primary_key=True)
#     sexo = db.Column(db.String)
#     edad = db.Column(db.Integer)
#     edad_anos_meses = db.Column(db.String)
#     residencia_pais_nombre = db.Column(db.String)
#     residencia_provincia_nombre = db.Column(db.String)
#     residencia_departamento_nombre = db.Column(db.String)
#     carga_provincia_nombre = db.Column(db.String)
#     fecha_inicio_sintomas = db.Column(db.DateTime)
#     fecha_apertura = db.Column(db.DateTime)
#     sepi_apertura = db.Column(db.Integer)
#     fecha_internacion = db.Column(db.DateTime)
#     cuidado_intensivo = db.Column(db.String)
#     fecha_cui_intensivo = db.Column(db.DateTime)
#     fallecido = db.Column(db.String)
#     fecha_fallecimiento = db.Column(db.DateTime)
#     asistencia_respiratoria_mecanica = db.Column(db.String)
#     carga_provincia_id = db.Column(db.Integer)
#     origen_financiamiento = db.Column(db.String)
#     clasificacion = db.Column(db.String)
#     clasificacion_resumen = db.Column(db.String)
#     residencia_provincia_id = db.Column(db.Integer)
#     fecha_diagnostico = db.Column(db.DateTime)
#     residencia_departamento_id = db.Column(db.Integer)
#     ultima_actualizacion = db.Column(db.DateTime)
