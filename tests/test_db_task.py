from unittest import TestCase
from task_manager.dbConnectors.mongoDbConnector import MongoDbConnector


class Evaluate(TestCase):

    def test_insert(self):
        data = {"_id": 2, "First name": "Andres"}
        mongo = MongoDbConnector("localhost,27017,db_task,test", [data])
        actual = mongo.insert()
        expected = {"response": "Data successfully inserted"}
        self.assertEqual(expected, actual)

    def test_select_all(self):
        mongo = MongoDbConnector("localhost,27017,db_task,test", [])
        actual = mongo.select_all()
        expected = None
        self.assertFalse(expected, actual)

    def test_select(self):
        data = {"_id": 2, "First name": "Andres"}
        mongo = MongoDbConnector("localhost,27017,db_task,test", ["2"])
        actual = mongo.select_by_id()
        expected = data
        self.assertEqual(expected, actual)

    def test_update(self):
        data = {
            "data": [
            {"_id": 2, "First name": "Andress"}
            ],
            "db_config": [
            {"db": "db_task", "collection": "test"}
            ]
            }
        mongo = MongoDbConnector("localhost,27017,db_task,test", ["2", data])
        actual = mongo.update()
        expected = {
             "response": "Document successfully updated"
                }
        self.assertEqual(expected, actual)

    # def test_delete(self):
    #     mongo = MongoDbConnector("localhost,27017,db_task,test", ["2"])
    #     mongo.delete()
    #     actual = mongo.select_by_id()
    #     expected = None
    #     self.assertEqual(expected, actual)
