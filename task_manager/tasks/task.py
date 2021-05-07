import sys
from abc import ABC, abstractmethod
from task_manager.configurations.baseConfiguration import BaseConfiguration
sys.path.append('../')


class Task(ABC):
    """
    Parent class defining general behaviour for all task objects

    ...

    Attributes
    ----------
    config: Configuration
        configuration object to be used in the task
    priority: int
        determines which task gets preference for executing first if more than one task are scheduled at the same time.

    Methods
    -------
    validate():
        Checks that all parameters are valid for task execution.
    """
    def __init__(self, config: BaseConfiguration, priority: int):
        self.config = config
        self.priority = priority

    def validate(self):
        """
        Checks that all parameters are valid for task execution.
        TODO
        """
        pass
