from tasks.task import Task
import sys
import requests
import json

sys.path.append('../')
from configurations.apiConfiguration import ApiConfiguration


class ApiTask(Task):
    """
    Child class of Task, defines specific methods for API tasks

    ...

    Attributes
    ----------
    config: Configuration
        configuration object to be used in the task
    priority: int
        determines which task gets preference for executing first if more than one task are scheduled at the same time.

    Methods
    -------
    execute():
        fires the execution chain for the request

    get_from_api():
        requests some data over the configured API

    post_to_api():
        requests some data over the configured API
    """

    def __init__(self, config: ApiConfiguration, priority: int):
        self.config = config
        self.priority = priority

    def execute(self):
        if self.config.rType == 'GET':
            self.get_from_api()
        elif self.config.rType == 'POST':
            self.validate()
            self.post_to_api()

    def get_from_api(self):
        """
        requests some data over the configured API
        """
        return requests.get(self.config.url)

    def post_to_api(self):
        """
        sends data to the configured API
        """
        json_data = json.dumps(self.config.data)
        return requests.post(self.config.url, json_data)

    def validate(self):
        """
        Checks that all parameters are valid for task execution.
        """
        try:
            json.dumps(self.config.data)
        except Exception as e:
            print('JSON Serialization for API Task failed!')
