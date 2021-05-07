import os


ROOT_DIR = os.path.abspath(os.curdir)

URLS = {
    "": "/api/path"
}

PATHS = {
    "default_api_task_config": os.path.abspath(f"{ROOT_DIR}/data/configurations/api/base_config_1.json"),
    "default_db_task_config": os.path.abspath(f"{ROOT_DIR}/data/configurations/db/base_config_1.json"),
    "default_file_task_config": os.path.abspath(f"{ROOT_DIR}/data/configurations/file/base_config_1.json")
}

def load_urls():
    return urls
