from flask import Flask
from flask import jsonify
from flask import request
from configurations.apiConfiguration import ApiConfiguration
from tasks.apiTask import ApiTask

def return_all_tasks():
    '''
    TODO
    :return:
    '''
    return 'TODO'

def return_one_task(name):
    '''
    TODO
    :return:
    '''
    return 'TODO'


def add_dummy_api_task():
    """
    TODO
    :return:
    """
    # LOAD CONFIG
    import json
    with open('../data/configurations/api/base_config_1.json') as json_file:
        d = json.load(json_file)
    credentials = d['credentials']
    url = d['url']
    r_type = d['r_type']
    cfg = ApiConfiguration(credentials, url, r_type)
    tsk = ApiTask(cfg, '', [])
    # TODO: Register task execution in DB
    # TODO: Register task execution in Scheduler

    return tsk.execute()


def add_api_task(config, priority, data):
    '''
    TODO
    :return:
    '''
    tsk = ApiTask(config, priority, data)
    return tsk.execute()

def edit_api_task(name):
    '''
    TODO
    :return:
    '''
    return 'TODO'

def delete_api_task(name):
    '''
    TODO
    :return:
    '''
    return 'TODO'
