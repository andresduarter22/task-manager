from task import Task
import sys
from enum import Enum
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
    get_from_api():
        requests some data over the configured API

    post_to_api():
        requests some data over the configured API
    """

    def __init__(self, config: ApiConfiguration, priority: int):
        self.config = config
        self.priority = priority

    def get_from_api(self):
        """
        requests some data over the configured API
        TODO
        """
        pass

    def post_to_api(self):
        """
        sends data to the configured API
        TODO
        """
        pass

    def validate(self):
        """
        Checks that all parameters are valid for task execution.
        TODO
        """
        pass
