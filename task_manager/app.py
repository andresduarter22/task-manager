"""Main module."""
from flask import Flask
from flask_restful import Api
from api_v1_0.resources.apiTaskEndpoints import ApiTaskEndpoints


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(ApiTaskEndpoints, "/api/v1/api_tasks", endpoint='api_tasks')

    return app

class TaskManagerApp(object):
    """
    Class that defines the Flask app behaviour and resources
    """
    def __init__(self):
        self.app = Flask(__name__)
        api = Api(self.app)
        api.add_resource(ApiTaskEndpoints, "/api/v1/api_tasks", endpoint='api_tasks')
        super(TaskManagerApp, self).__init__()

    def run(self):
        self.app.run(debug=True)

    def test_client(self):
        self.app.test_client()



if __name__ == '__main__':
    tm = TaskManagerApp()
    tm.run()
