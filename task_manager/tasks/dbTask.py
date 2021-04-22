from task import Task
import sys
from enum import Enum
sys.path.append('../')
from configurations.dbConfiguration import DbConfiguration


class DbTask(Task):
    """
    Child class of Task, defines specific methods for DB tasks

    ...

    Attributes
    ----------
    config: Configuration
        configuration object to be used in the task
    priority: int
        determines which task gets preference for executing first if more than one task are scheduled at the same time.

    Methods
    -------

    list_document():
        lists all entries in a DB table

    create_entry():
        creates a new entry with the set configuration

    update_entry():
        updates a DB entry

    delete_entry():
        removes a DB entry
    """

    def __init__(self, config: DbConfiguration, priority: int):
        self.config = config
        self.priority = priority

    def list_document(self):
        """
        lists all entries in a DB table
        TODO
        """
        pass

    def create_entry(self):
        """
        creates a new entry with the set configuration
        TODO
        """
        pass

    def update_entry(self):
        """
        requests some data over the configured API
        TODO
        """
        pass

    def delete_entry(self):
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
