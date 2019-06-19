from flask_restful import Resource
import logging as logger


class TaskById(Resource):

    def get(self, taskId):
        logger.debug("En get method por task by id. taskId = {}".format(taskId))
        return {"message": "En get method por task by id. taskId = {}".format(taskId)}, 200

    def post(self, taskId):
        logger.debug("EN post method por task by id. taskId = {}".format(taskId))
        return {"message": "En post method por task by id. taskId = {}".format(taskId)}, 200

    def put(self, taskId):
        logger.debug("En put method por task by id. taskId = {}".format(taskId))
        return {"message": "En put method por task by id. taskId = {}".format(taskId)}, 200

    def delete(self, taskId):
        logger.debug("En delete method por task by id. taskId = {}".format(taskId))
        return {"message": "En delete method por task by id. taskId = {}".format(taskId)}, 200
