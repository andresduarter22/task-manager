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

def test_new_task():
    """
    GIVEN the parameters for a task
    WHEN a new Task is created
    THEN check the config, priority and data fields are defined correctly
    """
    api_config = ApiConfiguration(load_default=True)
    api_task = ApiTask(config=api_config, priority=50, data=[{'random_key': 'some_value'}])
    assert api_task.config == api_config
    assert api_task.data == [{'random_key': 'some_value'}]
    assert api_task.priority == 50


def test_get_from_api():
    """
    GIVEN a configured task object with a valid request url
    WHEN the get_from_api method is called
    THEN check it returns a Response, with status code 200 and that the response.url is the same as config.url
    """
    api_config = ApiConfiguration(load_default=False,credentials={'usr': 'someUser', 'pwd': 'aHashedPassword'},
                                  url='http://httpbin.org/get', r_type='GET')

    api_task = ApiTask(config=api_config, priority=50, data=[{'random_key': 'some_value'}])
    result = api_task.get_from_api()
    assert type(result) == requests.Response
    assert result.url == api_config.url
    assert result.status_code == 200


def test_post_to_api():
    """
    GIVEN a configured task object with a valid request url
    WHEN the post_to_api method is called
    THEN check it returns a Response, with status code 200 and that the response.url is the same as config.url
    """
    api_config = ApiConfiguration(load_default=False, credentials={'usr': 'someUser', 'pwd': 'aHashedPassword'},
                                  url='http://httpbin.org/post', r_type='POST')

    api_task = ApiTask(config=api_config, priority=50, data=[{'random_key': 'some_value'}])
    result = api_task.post_to_api()
    assert type(result) == requests.Response
    assert result.url == api_config.url
    assert result.status_code == 200


def test_validate():
    """
    GIVEN a configured task object with valid data
    WHEN the validate method is called
    THEN check it returns a boolean with True value
    """
    api_config = ApiConfiguration(load_default=False, credentials={'usr': 'someUser', 'pwd': 'aHashedPassword'},
                                  url='http://httpbin.org/post', r_type='POST')

    api_task = ApiTask(config=api_config, priority=50, data=[{'random_key': 'some_value'}])
    result = api_task.validate()
    assert type(result) == bool
    assert result


def test_execute():
    """
    GIVEN a configured task object with a valid request url
    WHEN the execute method is called
    THEN check it returns a Response, with status code 200 and that the response.url is the same as config.url
    """
    api_config = ApiConfiguration(load_default=False, credentials={'usr': 'someUser', 'pwd': 'aHashedPassword'},
                                  url='http://httpbin.org/post', r_type='POST')

    api_task = ApiTask(config=api_config, priority=50, data=[{'random_key': 'some_value'}])
    result = api_task.execute()
    assert type(result) == requests.Response
    assert result.url == api_config.url
    assert result.status_code == 200
