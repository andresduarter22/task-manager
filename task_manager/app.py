"""Main module."""
from flask import Flask
from flask_restful import Api
from api_v1_0.resources.apiTaskEndpoints import ApiTaskEndpoints


class TaskManagerApp(object):
    """
    Class that defines the Flask app behaviour and resources
    """
    def __init__(self):
        self.app = Flask(__name__)
        api = Api(self.app)
        api.add_resource(ApiTaskEndpoints, "/api/v1/api_tasks", endpoint='api_tasks')

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    tm = TaskManagerApp()
    tm.run()
