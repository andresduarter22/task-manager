from abc import ABC, abstractmethod


class BaseConfiguration(ABC):
    """
    Parent class defining general behaviour for all configuration objects

    ...

    Attributes
    ----------
    data : list
        the data to be sent or returned

    Methods
    -------
    set_up():
        Prepares the configuration for being used when executing the task.
    """
    def __init__(self, data: list):
        self.data = data

    def set_up(self):
        """
        prepares the configuration for being used when executing the task.
        TODO
        """
        pass
