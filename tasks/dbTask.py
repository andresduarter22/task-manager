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
    db_mongo: str
        select the Database name to be used
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
    def __init__(self, config: DbConfiguration, priority: int, exec_type: object,  db_mongo: str = 'task_manager',
                 collection_mongo: str = 'test'):
        super().__init__(config, priority)
        self.config = config
        self.priority = priority
        self.db = db_mongo
        self.collection = collection_mongo
        self.exec_type = exec_type
        super.__init__(self)

    def list_document(self):
        """
        Calls select_all function of MongoDbConnector
        """
        mongo = MongoDbConnector(self.mongo_format())
        return mongo.select_all()

    def create_entry(self, document):
        """
        Calls insert function of MongoDbConnector
        """
        mongo = MongoDbConnector(self.mongo_format())
        res = mongo.insert(document)
        return res

    def update_entry(self, entry_id, new_value):
        """
        Calls update function of MongoDbConnector
        """
        mongo = MongoDbConnector(self.mongo_format())
        res = mongo.update(entry_id, new_value)
        return res

    def delete_entry(self, number):
        """
        Calls delete function of MongoDbConnector
        """
        mongo = MongoDbConnector(self.mongo_format())
        res = mongo.delete(number)
        return res

    def mongo_format(self):
        """
        Formats the connection string that mongoDbConnector needs
        """
        local = 'localhost'
        port = '27017'
        res = local + ',' + port + ',' + self.db + ',' + self.collection
        return res
