"""Main module."""
from configurations.apiConfiguration import ApiConfiguration
from tasks.apiTask import ApiTask
from configurations.fileConfiguration import FileConfiguration
from tasks.fileTask import FileTask

if __name__ == "__main__":
    """Main"""
    #-----RUNNING API TASK-----
    # data = [{'name': "John", 'age': 31, 'city': "New York"}]
    # query = ''
    # credentials = None
    # url = 'https://httpbin.org/get'
    # #url = 'https://httpbin.org/post'
    # # url = 'httpbin.org/put'
    # # url = 'httpbin.org/delete'
    # rType = 'GET'
    # newConfig = ApiConfiguration(data, query, credentials, url, rType)
    # myTask = ApiTask(newConfig, 100)
    # print(myTask.__dict__)
    #---------------------------

    #RUNNING FILE TASK
    directory = '../files'
    #filename = 'test_json.json'
    #filename = 'test_yaml.yaml'
    filename = 'new_test_json.yaml'
    f_type = 'JSON'
    #f_type = 'YAML'
    #is_writing = False
    is_writing = True

    #yaml_data = [[{'sports': ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
    #              {'countries': ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]]

    json_data = {'people': []}
    json_data['people'].append({
        'name': 'Scott',
        'website': 'stackabuse.com',
        'from': 'Nebraska'
    })
    json_data['people'].append({
        'name': 'Larry',
        'website': 'google.com',
        'from': 'Michigan'
    })
    json_data['people'].append({
        'name': 'Tim',
        'website': 'apple.com',
        'from': 'Alabama'
    })

    f_conf = FileConfiguration(directory, filename, f_type, is_writing)
    my_task = FileTask(f_conf, 100, json_data)
    print(my_task.execute())
