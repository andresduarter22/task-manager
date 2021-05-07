import sys
from abc import ABC, abstractmethod
import uuid

sys.path.append('../../')
from configurations.baseConfiguration import BaseConfiguration



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
    exec_type : ExecutionType
        defines the execution type
    task_id: str
        defines the unique identifier for the task

    Methods
    -------
    validate():
        Checks that all parameters are valid for task execution.
    """
    def __init__(self, config: BaseConfiguration, priority: int):
        self.config = config
        self.priority = priority
        self.task_id = uuid.uuid4().hex

    def validate(self):
        """
        Checks that all parameters are valid for task execution.
        TODO
        """
        pass
