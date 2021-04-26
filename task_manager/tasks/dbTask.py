import sys
import pprint
from pymongo import MongoClient
from task_manager.tasks.task import Task
from task_manager.configurations.dbConfiguration import DbConfiguration
from task_manager.dbConnectors.mongoDbConnector import MongoDbConnector

sys.path.append('../')

try:
    client = MongoClient('localhost', 27017)
except Exception as e:
    print('Cannot connect to Mongo client.')


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

    def __init__(self, config: DbConfiguration, priority: int, db_mongo, collection_mongo):
        self.config = config
        self.priority = priority
        self.db = db_mongo
        self.collection = collection_mongo

    def list_document(self):
        res = []
        db = client[self.db]
        collection = db[self.collection]
        for info in collection.find():
            res.append(info)
            pprint.pprint(info)
        print("It works!", self.db, self.collection)
        return res

    def create_entry(self, document):
        mongo_connector = MongoDbConnector
        mongo_connector.connect()
        db = client[self.db]
        collection = db[self.collection]
        collection.insert_one(document)

    def update_entry(self, entry_id, new_value):
        db = client[self.db]
        collection = db[self.collection]
        old = {
            'id': entry_id
        }
        new = {"$set": new_value}
        collection.update_one(old, new)

    def delete_entry(self, number):
        db = client[self.db]
        collection = db[self.collection]
        collection.delete_one({'number': number})

    def validate(self):
        """
        Checks that all parameters are valid for task execution.
        TODO
        """
        pass
