from configurations.queryBasedConfiguration import QueryBasedConfiguration
from enum import Enum


class ApiMethods(Enum):
    POST = 1
    GET = 2
    PUT = 3


class ApiConfiguration(QueryBasedConfiguration):
    """
    Child class of QueryBasedConfigurations, defines specific methods for configuring API requests

    ...

    Attributes
    ----------
    data : list
        the data to be sent or returned to the API
    query : str
        the query string to execute in the DB/send request to API
    credentials : dict
        the login credentials
    url : string
        the URL of the API
    type : ApiMethods
        the method to use in the request

    Methods
    -------
    set_up():
        Prepares the configuration for being used when executing the task.
    """
    def __init__(self, data: list, query: str, credentials: dict, url: str, rType: str):
        self.data = data
        self.query = query
        self.credentials = credentials
        self.url = url
        self.rType = rType


    def set_up(self):
        """
        prepares the configuration for being used when executing the task.
        TODO
        """
        pass
