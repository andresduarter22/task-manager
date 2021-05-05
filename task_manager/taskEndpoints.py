import pprint

from flask import jsonify, request
from task_manager.tasks.dbTask import DbTask
from task_manager.configurations.dbConfiguration import DbConfiguration, DbTypeList


class Endpoints:

    @staticmethod
    def select_insert_db():
        type_db = DbTypeList(1)
        config = DbConfiguration([request.get_json()], "str", {}, "task_manager", type_db)
        task = DbTask(config, 1)
        endpoint_request = request.get_json()
        if request.method == 'GET':
            response = jsonify(task.list_document())
            return response
        else:
            response = jsonify(task.create_entry(endpoint_request))
            return response

    @staticmethod
    def update_delete_db():
        type_db = DbTypeList(1)
        config = DbConfiguration([request.get_json()], "str", {}, "task_manager", type_db)
        task = DbTask(config, 1)
        endpoint_request = request.get_json()
        if request.method == 'PUT':
            response = jsonify(task.update_entry())
            return response
        else:
            response = jsonify(task.create_entry(endpoint_request))
            return response
