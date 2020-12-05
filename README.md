# How to run?
####Install requirements
```
pip install -r requirements.txt
```
``` 
pip install -e . # nunca lo use
```
####Ru the api
```
python -m covidapi
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