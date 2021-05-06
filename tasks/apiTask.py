from tasks.task import Task
import sys
import requests
import json

sys.path.append('../')
from utils.logger import CustomLogger
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
    exec_type  : str
        defines the execution type
    task_id: str
        defines the unique identifier for the task

    Methods
    -------
    execute():
        fires the execution chain for the request

    get_from_api():
        requests some data over the configured API

    post_to_api():
        requests some data over the configured API
    """

    def __init__(self, config: ApiConfiguration, priority: int, data: list):
        self.logger = CustomLogger(__name__)
        self.config = config
        self.priority = priority
        self.data = data
        # self.exec_type = exec_type
        super(ApiTask, self).__init__(self.config, self.priority, self.data)

    def execute(self):
        if self.config.r_type == 'GET':
            self.get_from_api()
        elif self.config.r_type == 'POST':
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
        print(f'pre-jason: {self.data}')
        json_data = json.dumps(self.data)
        print(f'DATAAA: {json_data}')
        return requests.post(self.config.url, json_data)

    def validate(self):
        """
        Checks that all parameters are valid for task execution.
        """
        try:
            json.dumps(self.data)
        except Exception as e:
            print('JSON Serialization for API Task failed!')
