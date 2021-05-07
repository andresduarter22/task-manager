from flask import jsonify
from task_manager.tasks.dbTask import DbTask
from task_manager.configurations.dbConfiguration import DbConfiguration
from flask_restful import Resource, reqparse


class TaskDBEndpointsId(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=dict), parser.add_argument('db_config', type=dict)
        self.parser = parser
        self.request_data = self.parser.parse_args()
        self.selected_db, self.selected_collection, = \
            self.request_data["db_config"]["db"], self.request_data["db_config"]["collection"]
        self.document = self.request_data["data"]

    def get(self, id_db):
        config = DbConfiguration([id_db], "get", {}, self.selected_db)
        task = DbTask(config, 1, self.selected_collection)
        response = jsonify(task.list_one())
        # redis (id, "TASK", "user", "asap", exec_time, "DB", self.selected_db, "MONGO",
        # "test", response, response_success, 1, request.get_json())
        return response

    def put(self, id_db):
        config = DbConfiguration([id_db, self.document], "put", {}, self.selected_db)
        task = DbTask(config, 1, self.selected_collection)
        response = jsonify(task.update_entry())
        return response

    def delete(self, id_db):
        config = DbConfiguration([id_db], "delete", {}, self.selected_db)
        task = DbTask(config, 1, self.selected_collection)
        response = jsonify(task.delete_entry())
        return response


class TaskDBEndpoints(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=dict), parser.add_argument('db_config', type=dict)
        self.parser = parser
        self.request_data = self.parser.parse_args()
        self.selected_db, self.selected_collection,  = \
            self.request_data["db_config"]["db"], self.request_data["db_config"]["collection"]
        self.document = self.request_data["data"]

    def get(self):
        config = DbConfiguration([None], "get", {}, self.selected_db)
        task = DbTask(config, 1, self.selected_collection)
        response = jsonify(task.list_document())
        return response

    def post(self):
        config = DbConfiguration([self.document], "post", {}, self.selected_db)
        task = DbTask(config, 1, self.selected_collection)
        response = jsonify(task.create_entry())
        return response
