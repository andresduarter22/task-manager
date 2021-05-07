from task_manager.configurations.queryBasedConfiguration import QueryBasedConfiguration
from enum import Enum


class DbConfiguration(QueryBasedConfiguration):
    """
    Child class of QueryBasedConfigurations, defines specific methods for configuring DB queries

    ...

    Attributes
    ----------
    data : list
        the data to be sent or returned to the API
    query : str
        the query string to execute in the DB/send request to API
    credentials : dict
        the login credentials
    db_name : string
        name of the DB to be accessed
    type : ApiMethods
        the method to use in the request

    Methods
    -------
    set_up():
        Prepares the configuration for being used when executing the task.
    """

    def __init__(self, data: list, query: str, credentials: dict, db_name: str):
        self.data = data
        self.query = query
        self.credentials = credentials
        self.db_name = db_name
        self.type = type

    def set_up(self):
        """
        prepares the configuration for being used when executing the task.
        TODO
        """
        pass
