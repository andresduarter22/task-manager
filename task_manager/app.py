"""Main module."""
from configurations.apiConfiguration import ApiConfiguration
from tasks.apiTask import ApiTask
from configurations.fileConfiguration import FileConfiguration
from tasks.fileTask import FileTask
import taskEndpoints
import json
from flask import Flask
import time, threading
from utils.configuration import Configuration
from execution.scheduler import Scheduler

app = Flask(__name__)

app.add_url_rule('/tasks/api/add', methods=['POST'], view_func=taskEndpoints.add_api_task)

if __name__ == '__main__':
    cfg = Configuration()
    scheduler_update_timer = cfg.get_config_var('scheduler_refresh_rate_ms')
    print(scheduler_update_timer)
    app.run(debug=True, use_reloader=True)

    threading.Timer(10, application.reset()).start()
    time.sleep(scheduler_update_timer)
    print('update 1')
    time.sleep(scheduler_update_timer)
    print('update 2')
    time.sleep(scheduler_update_timer)
    print('update 3')
