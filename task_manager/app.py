"""Main module."""
from configurations.apiConfiguration import ApiConfiguration
from tasks.apiTask import ApiTask
from configurations.fileConfiguration import FileConfiguration
from tasks.fileTask import FileTask
import taskEndpoints
import json
from flask import Flask


app = Flask(__name__)

app.add_url_rule('/tasks/api/add', methods=['POST'], view_func=taskEndpoints.add_api_task)

if __name__ == '__main__':

    app.run(debug=True, use_reloader=True)
