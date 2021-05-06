"""
Defines general behaviour for all query-based configuration objects

Classes:

    QueryBasedConfiguration

Functions:

    set_up(object)

Misc variables:

    data
    query
    credentials
"""
from configurations.baseConfiguration import BaseConfiguration


class QueryBasedConfiguration(BaseConfiguration):
    """
    Defines general behaviour for all query-based configuration objects
    Parent class for ApiConfiguration and DbConfiguration classes
    child class of Configuration

    ...

    Attributes
    ----------
    data : list
        the data to be sent or returned
    query : str
        the query string to execute in the DB/send request to API
    credentials : dict
        the login credentials

    Methods
    -------
    set_up():
        Prepares the configuration for being used when executing the task.
    """
    def __init__(self, data: list, query: str, credentials: dict):
        self.data = data
        self.query = query
        self.credentials = credentials

    def set_up(self):
        """
        prepares the configuration for being used when executing the task.
        TODO
        """
        pass
