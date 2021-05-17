import sys
from task_manager.tasks.task import Task
from task_manager.configurations.dbConfiguration import DbConfiguration
from task_manager.dbConnectors.mongoDbConnector import MongoDbConnector

sys.path.append('../')


class DbTask(Task):
    """
    Child class of Task, defines specific methods for DB tasks

    ...

    Attributes
    ----------
    config: Configuration
        configuration object to be used in the task
    priority: int
        determines which task gets preference for executing first if more than one task are scheduled at the same time.
    collection_mongo: str
        select the collection name to be used
    exec_type  : str
        defines the execution type
    task_id: str
        defines the unique identifier for the task

    Methods
    -------

    list_document():
        lists all entries in a DB table

    create_entry():
        creates a new entry with the set configuration

    update_entry():
        updates a DB entry

    delete_entry():
        removes a DB entry
    """

    def __init__(self, config: DbConfiguration, priority: int, collection_mongo: str = 'test'):
        super().__init__(config, priority)
        self.config = config
        self.priority = priority
        self.db = config.db_name
        self.collection = collection_mongo

        self.mongo = MongoDbConnector(self.mongo_format(), self.config.data)

    def list_document(self):
        """
        Calls select_all function of MongoDbConnector
        """
        return self.mongo.select_all()

    def list_one(self):
        """
        Calls select_all function of MongoDbConnector
        """
        return self.mongo.select_by_id()

    def create_entry(self):
        """
        Calls insert function of MongoDbConnector
        """
        response = self.mongo.insert()
        return response

    def update_entry(self):
        """
        Calls update function of MongoDbConnector
        """
        response = self.mongo.update()
        return response

    def delete_entry(self):
        """
        Calls delete function of MongoDbConnector
        """
        response = self.mongo.delete()
        return response

    def mongo_format(self):
        """
        Formats the connection string that mongoDbConnector needs
        """
        local, port = 'mongo', '27017'
        response = local + ',' + port + ',' + self.db + ',' + self.collection
        return response
