from flask import Flask
from flask_restful import Resource, reqparse
from flask import jsonify
from flask import request
from configurations.apiConfiguration import ApiConfiguration
from tasks.apiTask import ApiTask
import redis
import definitions
from dbConnectors.redisDbConnector import RedisDbConnector


class ApiTaskListEndpoints(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('config', type=dict, default={"credentials": {}, "url": "https://httpbin.org/post", "r_type": "POST"}, location='json')
        self.reqparse.add_argument('data', type=list, default=[], location='json')
        self.reqparse.add_argument('priority', type=int, default=100, location='json')
        super(ApiTaskListEndpoints, self).__init__()
        self.r = RedisDbConnector('server=localhost,db=0,port=6379')
        #self.r.insert('1', 'test')

    def get(self):
        return jsonify(self.r.keys())

    def post(self):
        args = self.reqparse.parse_args()
        post_data = {
            'config': [args['config']],
            'data': [args['data']],
            'priority': [args['priority']]
        }
        print(post_data)
        cfg = ApiConfiguration(load_default=True) #TEST ONLY

        res = ApiTask(cfg,  priority=post_data['priority'], data=post_data['data']).execute()

        return {res}, 201


class ApiTaskEndpoints(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=str, required=True, help='No id provided', location='json')
        self.reqparse.add_argument('config', type=str, location='json')
        self.reqparse.add_argument('data', type=str, location='json')
        self.reqparse.add_argument('priority', type=bool, location='json')
        super(ApiTaskEndpoints, self).__init__()

    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass



