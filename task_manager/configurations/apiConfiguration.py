from task_manager.configurations.queryBasedConfiguration import QueryBasedConfiguration


class ApiConfiguration(QueryBasedConfiguration):
    """
    Child class of QueryBasedConfigurations, defines specific methods for configuring API requests

    ...

    Attributes
    ----------
    load_default : bool
        defines if the default config is loaded
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
    def __init__(self, load_default: bool, credentials: dict = None, url: str = None, r_type: str = None):
        """
        Initalizes the configuration object, either from a default JSON config file or from the parameters passed

        :param load_default: bool that determines if the configuration is loaded from a default file or not.
        :param credentials: OPTIONAL authentication info
        :param url: OPTIONAL - url for the api request
        :param r_type: OPTIONAL GET or POST request
        """
        if load_default:
            import json
            with open(defs.PATHS['default_api_task_config']) as json_file:
                data = json.load(json_file)
                self.credentials = data['credentials']
                self.url = data['url']
                self.r_type = data['r_type']
        else:
            self.credentials = credentials
            self.url = url
            self.r_type = r_type

    def set_up(self):
        """
        prepares the configuration for being used when executing the task.
        TODO
        """
        pass

