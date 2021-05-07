from flask_restful import Resource, reqparse
from flask import jsonify
from flask import request, abort
from configurations.apiConfiguration import ApiConfiguration
from task_manager.tasks.apiTask import ApiTask
import ast


class ApiTaskEndpoints(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('config', type=dict)
        self.reqparse.add_argument('data', type=list)
        self.reqparse.add_argument('priority', type=int)
        super(ApiTaskEndpoints, self).__init__()

    def get(self):
        """
        gets from api

        :returns dictionary {id: task_info}
        """
        print('ENTERED')
        #args = self.reqparse.parse_args()
        try:
            config = ast.literal_eval(request.args['config'])
        except():
            abort(400)

        try:
            data = request.args['data']
        except():
            pass

        try:
            priority = request.args['priority']
        except():
            pass

        cfg = ApiConfiguration(load_default=False, url=config['url'], r_type=config['r_type'])
        tsk = ApiTask(cfg, priority=priority, data=data)
        response = tsk.execute()
        return jsonify(response.reason, response.status_code)

    def post(self):
        """
        posts to an API

        :returns
        Response.reason :string - describes the status_code returned from the API Request
        Response.status_code :int - status_code returned from the API Request
        """
        try:
            config = ast.literal_eval(request.args['config'])
        except():
            abort(400)

        try:
            data = request.args['data']
        except():
            pass

        try:
            priority = request.args['priority']
        except():
            pass

        cfg = ApiConfiguration(load_default=False, url=config['url'], r_type=config['r_type'])
        tsk = ApiTask(cfg, priority=priority, data=data)
        response = tsk.execute()

        return jsonify(response.reason, response.status_code)

