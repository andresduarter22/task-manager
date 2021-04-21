from baseConfiguration import BaseConfiguration
from enum import Enum


class FileTypeList(Enum):
    CSV = 1
    YAML = 2
    JSON = 3
    XML = 4


class FileConfiguration(BaseConfiguration):
    """
    Defines general behaviour for all file configuration objects
    child class of Configuration

    ...

    Attributes
    ----------
    data : list
        the data to be sent or returned
    directory : str
        the query string to execute in the DB/send request to API
    f_type : FileTypeList
        the login credentials

    Methods
    -------
    set_up():
        Prepares the configuration for being used when executing the task.
    """
    def __init__(self, data: list, directory: str, f_type: FileTypeList):
        self.data = data
        self.directory = directory
        self.f_type = f_type

    def set_up(self):
        """
        prepares the configuration for being used when executing the task.
        TODO
        """
        pass
