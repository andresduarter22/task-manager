from task_manager.configurations.baseConfiguration import BaseConfiguration


class FileConfiguration(BaseConfiguration):
    """
    Defines general behaviour for all file configuration objects
    child class of Configuration

    ...

    Attributes
    ----------
    directory : str
        the query string to execute in the DB/send request to API
    f_type : FileTypeList
        the login credentials
    is_writing: bool
        variable that stores whether the current task is writing or reading a file

    Methods
    -------
    set_up():
        Prepares the configuration for being used when executing the task.
    """
    def __init__(self, directory: str, filename: str, f_type: str, is_writing: bool):
        self.directory = directory
        self.filename = filename
        self.f_type = f_type
        self.is_writing = is_writing

    def set_up(self):
        """
        prepares the configuration for being used when executing the task.
        TODO
        """
        pass
