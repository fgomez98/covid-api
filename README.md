# How to run?

#### Install requirements

```
pip install -r requirements.txt
```

or

``` 
pip install -e . # nunca lo use
```

#### Run the api

```
python -m covidapi
```

or

```
export FLASK_APP=covidapi/api
export FLASK_ENV=development
flask run   
```  

#### Samples

```
curl -X GET -H "Content-Type: application/json"  http://127.0.0.1:5000/bar/ -d '{"name": "Juan", "age": 21}'
curl -X POST -H "Content-Type: application/json"  http://127.0.0.1:5000/bar/ -d '{"name": "Pablo", "age": 42}'
curl -X GET http://127.0.0.1:5000/bar/
curl -X POST http://127.0.0.1:5000/foo/titi_henry/
curl -X GET http://127.0.0.1:5000/foo/titi_henry/
curl -X DELETE http://127.0.0.1:5000/foo/titi_henry/
```     

#### Acces swagger Documentation on

http://localhost:5000/api/spec.html or `curl http://localhost:5000/api/spec.json`

#### Usefull Links

- https://flask.palletsprojects.com/en/1.1.x/
- https://flask-restful-swagger.readthedocs.io/en/latest/articles/README.html#how-to
- https://flask-restful.readthedocs.io/en/latest/
- http://datos.salud.gob.ar/dataset/covid-19-casos-registrados-en-la-republica-argentina
- http://datos.salud.gob.ar/dataset/covid-19-casos-registrados-en-la-republica-argentina/archivo/fd657d02-a33a-498b-a91b-2ef1a68b8d16
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/