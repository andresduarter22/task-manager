import json
from pymongo import MongoClient
from task_manager.dbConnectors.abstractDbConnector import AbstractDbConnector


class MongoDbConnector(AbstractDbConnector):
    """
    Defines all the necessary behaviour for connecting to a Mongo DB
    and performing the requested operations.
    ...

    Attributes
    ----------
    connection_string : str
        the string with all information necessary to connect to the db

    Methods
    -------
    connect():
        Tries to reach the DB and connect to it.

    insert():
        Inserts the given data to a db document.

    update():
        Updates some entry in a db document

    delete():
        deletes an entry in a db document

    validate():
        validates if the input data is the right format

    """

    def __init__(self, connection_string):
        super().__init__(connection_string)
        self.connection_string = connection_string
        self.host, self.port, self.db, self.collection = self.parse_connection_string()
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.db]
        self.collection = self.db[self.collection]

    def parse_connection_string(self):
        values = self.connection_string.split(',')
        host, port, db, collection = values[0], int(values[1]), values[2], values[3]
        return host, port, db, collection

    def select_all(self):
        collection = self.collection
        response = [info for info in collection.find()]
        self.client.close()
        return response

    def insert(self, document):
        collection = self.collection
        self.validate(document)
        collection.insert_one(document)
        self.client.close()
        return "Data successfully inserted"

    def update(self, entry_id, new_value):
        collection = self.collection
        self.validate(new_value)
        old = {
            'id': entry_id
        }
        new = {"$set": new_value}
        collection.update_one(old, new)
        self.client.close()
        return "Document successfully updated"

    def delete(self, id_entry):
        collection = self.collection
        collection.delete_one({'id': id_entry})
        return "Document successfully deleted"

    @staticmethod
    def validate(document):
        try:
            a_json = json.loads(document)
            print(a_json)
        except:
            print("Data isn't a JSON")
