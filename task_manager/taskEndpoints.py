from flask import jsonify, request
from task_manager.tasks.dbTask import DbTask
from task_manager.configurations.dbConfiguration import DbConfiguration, DbTypeList


class Endpoints:

    @staticmethod
    def select_insert_db():
        type_db = DbTypeList(1)
        config = DbConfiguration([request.get_json()], "str", {}, "task_manager", type_db)
        task = DbTask(config, 1)
        if request.method == 'GET':
            response = jsonify(task.list_document())
            return response
        elif request.method == 'POST':
            response = jsonify(task.create_entry())
            return response

    @staticmethod
    def update_delete_db(id_db):
        type_db = DbTypeList(1)
        config = DbConfiguration([id_db, request.get_json()], "str", {}, "task_manager", type_db)
        task = DbTask(config, 1)
        if request.method == 'PUT':
            response = jsonify(task.update_entry())
            return response
        elif request.method == 'DELETE':
            response = jsonify(task.delete_entry())
            return response
