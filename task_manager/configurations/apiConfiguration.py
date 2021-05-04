from configurations.queryBasedConfiguration import QueryBasedConfiguration


class ApiConfiguration(QueryBasedConfiguration):
    """
    Child class of QueryBasedConfigurations, defines specific methods for configuring API requests

    ...

    Attributes
    ----------
    credentials : dict
        the login credentials
    url : string
        the URL of the API
    r_type : ApiMethods
        the method to use in the request

    Methods
    -------
    set_up():
        Prepares the configuration for being used when executing the task.
    """
    def __init__(self, credentials: dict, url: str, r_type: str):
        self.credentials = credentials
        self.url = url
        self.r_type = r_type


    def set_up(self):
        """
        prepares the configuration for being used when executing the task.
        TODO
        """
        pass
