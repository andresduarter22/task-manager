from task_manager.tasks.task import Task
import sys
import requests
import json

sys.path.append('../../')
from task_manager.configurations.apiConfiguration import ApiConfiguration



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

    def __init__(self, config: object, priority: int, data: list):
        """
        Initializes the API Task object
        :param config: ApiConfiguration object
        :param priority: priority to be executed (only used in executionQueue)
        :param data: data to send to the API Request
        """
        #self.logger = CustomLogger(__name__)
        self.config = config
        self.priority = priority
        self.data = data
        # self.exec_type = exec_type
        super(ApiTask, self).__init__(self.config, self.priority)

    def execute(self):
        """
        executes the task, based on the type specified in its configuration object

        :returns Response attributes fetched from get_from_api() or post_to_api().
        """
        if self.config.r_type == 'GET':
            return self.get_from_api()
        elif self.config.r_type == 'POST':
            self.validate()
            return self.post_to_api()
        else:
            return None

    def get_from_api(self):
        """
        requests some data over the configured API

        :returns Response from the request.get()
        """
        return requests.get(self.config.url)

    def post_to_api(self):
        """
        sends data to the configured API

        :returns Response from the request.post()
        """
        json_data = json.dumps(self.data)
        return requests.post(self.config.url, json_data)

    def validate(self):
        """
        Checks that all parameters are valid for task execution.
        """
        correct = False
        try:
            json.dumps(self.data)
            correct=True
        except Exception as e:
            print('JSON Serialization for API Task failed!')
        return correct
