from task import Task
import sys
import json
import yaml


sys.path.append('../')
from configurations.fileConfiguration import FileConfiguration


class FileTask(Task):
    """
    Child class of Task, defines specific methods for File-reading tasks

    ...

    Attributes
    ----------
    config: Configuration
        configuration object to be used in the task
    priority: int
        determines which task gets preference for executing first if more than one task are scheduled at the same time.

    Methods
    -------

    read_json():
        reads a json file

    write_json():
        writes a json file

    read_yaml():
        reads a yaml file

    write_yaml():
        writes a yaml file
    """

    def __init__(self, config: FileConfiguration, priority: int,  data: list, is_writing: bool):
        self.config = config
        self.priority = priority
        self.data = data
        self.is_writing = is_writing

    def read_json(self):
        """
        reads JSON File
        """
        self.data = []
        with open(f'{self.config.directory}/{self.config.filename}') as json_file:
            self.data.append(json.load(json_file))

        return self.data

    def write_json(self):
        """
        creates a new json file with the loaded data
        """
        with open(f'{self.config.directory}/{self.config.filename}') as json_file:
            json.dump(self.data[0], json_file)

    def read_yaml(self):
        """
        reads a YAML file
        """
        self.data = []
        with open(f'{self.config.directory}/{self.config.filename}') as yaml_file:
            self.data.append(yaml.load(yaml_file, Loader=yaml.FullLoader))
        return self.data

    def write_yaml(self):
        """
        writes a YAML file with the loaded data
        """
        with open(f'{self.config.directory}/{self.config.filename}', 'w') as yaml_file:
            self.data = yaml.dump(self.data[0], yaml_file)

    def validate(self):
        """
        Checks that all parameters are valid for task execution.
        """
        if self.config.f_type == 'YAML':
            if self.is_writing:
                try:
                    yaml.load(self.data)
                except yaml.YAMLError as e:
                    print(e)
            else:
                try:
                    with open(f'{self.config.directory}/{self.config.filename}', 'r') as yaml_file:
                        yaml_data = yaml_file.read()
                    yaml.safe_load(yaml_data)
                except yaml.YAMLError as e:
                    print(e)

        elif self.config.f_type == 'JSON':
            if self.is_writing:
                try:
                    json.dumps(self.data)
                except json.JSONDecodeError as e:
                    print(e)
            else:
                try:
                    with open(f'{self.config.directory}/{self.config.filename}', 'r') as json_file:
                        json_data = json_file.read()
                    json.loads(json_data)
                except yaml.YAMLError as e:
                    print(e)
