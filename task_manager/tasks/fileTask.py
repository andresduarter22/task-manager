from task import Task
import sys
from enum import Enum

sys.path.append('../')
from configurations.fileConfiguration import FileConfiguration


class FileTask(Task):
    """
    Child class of Task, defines specific methods for File-reading tasks

    ...

    Attributes
    ----------
    config: Configuration
        configuration object to be used in the task
    priority: int
        determines which task gets preference for executing first if more than one task are scheduled at the same time.

    Methods
    -------

    read_json():
        reads a json file

    write_json():
        writes a json file

    read_yaml():
        reads a yaml file

    write_yaml():
        writes a yaml file
    """

    def __init__(self, config: FileConfiguration, priority: int):
        self.config = config
        self.priority = priority

    def read_json(self):
        """
        lists all entries in a DB table
        TODO
        """
        pass

    def write_json(self):
        """
        creates a new entry with the set configuration
        TODO
        """
        pass

    def read_yaml(self):
        """
        requests some data over the configured API
        TODO
        """
        pass

    def write_yaml(self):
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
