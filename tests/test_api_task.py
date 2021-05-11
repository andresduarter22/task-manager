import requests

from task_manager.tasks.apiTask import ApiTask
from task_manager.configurations.apiConfiguration import ApiConfiguration

def test_new_config():
    """
    GIVEN configuration data
    WHEN a new Config is created
    THEN check the load_default, credentials, url, r_type fields are defined correctly
    """
    api_config = ApiConfiguration(load_default=False,credentials={'usr': 'someUser', 'pwd': 'aHashedPassword'}, url='www.google.com.bo', r_type='POST')
    assert api_config.credentials == {'usr': 'someUser', 'pwd': 'aHashedPassword'}
    assert api_config.url == 'www.google.com.bo'
    assert api_config.r_type == 'POST'

def test_new_default_config():
    """
    GIVEN no configuration data
    WHEN a new Config is created
    THEN check the load_default, credentials, url, r_type fields are defined correctly
    """
    api_config = ApiConfiguration(load_default=True)
    assert api_config.credentials == {}
    assert api_config.url == "https://httpbin.org/post"
    assert api_config.r_type == 'POST'
