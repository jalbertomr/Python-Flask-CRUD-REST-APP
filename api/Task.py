from flask_restful import Resource
import logging as logger

class Task(Resource):

    def get(self):
        logger.debug("En get method")
        return {"message": "En get method"}, 200

    def post(self):
        logger.debug("EN post method")
        return {"message": "En post method"}, 200

    def put(self):
        logger.debug("En put method")
        return {"message": "En put method"}, 200

    def delete(self):
        logger.debug("En delete method")
        return {"message": "En delete method"}, 200