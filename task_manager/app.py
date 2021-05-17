"""Main module."""
from flask import Flask
from flask_restful import Api
from api_v1_0.resources.apiTaskEndpoints import ApiTaskEndpoints
from task_manager.taskEndpoints import TaskDBEndpoints, TaskDBEndpointsId


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(ApiTaskEndpoints, "/api/v1/api_tasks", endpoint='api_tasks')
    api.add_resource(TaskDBEndpoints, "/api/v1/tasks/db", endpoint='db')
    api.add_resource(TaskDBEndpointsId, "/api/v1/tasks/db/<int:id_db>")
    return app


class TaskManagerApp(object):
    """
    Class that defines the Flask app behaviour and resources
    """
    def __init__(self):
        self.app = Flask(__name__)
        api = Api(self.app)
        api.add_resource(ApiTaskEndpoints, "/api/v1/api_tasks", endpoint='api_tasks')
        api.add_resource(TaskDBEndpoints, "/api/v1/tasks/db", endponit='db')
        api.add_resource(TaskDBEndpointsId, "/api/v1/tasks/db/<int:id_db>")
        super(TaskManagerApp, self).__init__()

    def run(self):
        self.app.run(debug=True)

    def test_client(self):
        self.app.test_client()


if __name__ == '__main__':
    tm = TaskManagerApp()
    tm.run()
