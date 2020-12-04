from flask_restful import abort

def raise_general_error():
    abort(404, message="Ups, something went wrong")