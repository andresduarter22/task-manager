"""Main module."""
from configurations.apiConfiguration import ApiConfiguration
from tasks.apiTask import ApiTask
from configurations.fileConfiguration import FileConfiguration
from tasks.fileTask import FileTask
import json
from flask import Flask
from utils.configuration import Configuration
from flask_restful import Api
from api_v1_0.resources.apiTaskEndpoints import ApiTaskListEndpoints, ApiTaskEndpoints


class TaskManagerApp(object):
    def __init__(self):
        self.app = Flask(__name__)
        api = Api(self.app)
        api.add_resource(ApiTaskListEndpoints, "/api/v1/api_tasks", endpoint='api_tasks')
        api.add_resource(ApiTaskEndpoints, "/api/v1/api_task/<int:id>", endpoint='api_task')

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    tm = TaskManagerApp()
    tm.run()
