"""Main module."""
from task_manager.taskEndpoints import TaskDBEndpoints, TaskDBEndpointsId
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
api.add_resource(TaskDBEndpoints, '/api/v1/tasks/db')
api.add_resource(TaskDBEndpointsId, '/api/v1/tasks/db/<int:id_db>')

if __name__ == '__main__':
    app.run()
