from task_manager.app import create_app
from api_v1_0.resources.apiTaskEndpoints import ApiTaskEndpoints

def test_api_task_get():
    """
    GIVEN a Flask application running on the local machine
    WHEN the /api/v1/api_tasks page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('http://127.0.0.1:5000/api/v1/api_tasks?config={"load_default":"False","url":"http://httpbin.org/get","r_type":"GET"}&data=[]&priority=100')
        assert response.status_code == 200


def test_api_task_post():
    """
    GIVEN a Flask application running on the local machine
    WHEN the /api/v1/api_tasks page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('http://127.0.0.1:5000/api/v1/api_tasks?config={"load_default":"False","url":"http://httpbin.org/get","r_type":"GET"}&data=[]&priority=100')
        assert response.status_code == 200
