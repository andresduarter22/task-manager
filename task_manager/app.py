"""Main module."""
from configurations.apiConfiguration import ApiConfiguration
from tasks.apiTask import ApiTask

if __name__ == "__main__":
    """Main"""
    data = [{'name': "John", 'age': 31, 'city': "New York"}]
    query = ''
    credentials = None
    #url = 'https://httpbin.org/get'
    url = 'https://httpbin.org/post'
    # url = 'httpbin.org/put'
    # url = 'httpbin.org/delete'
    rType = 'POST'
    newConfig = ApiConfiguration(data, query, credentials, url, rType)
    myTask = ApiTask(newConfig, 100)
    print(myTask.execute())
