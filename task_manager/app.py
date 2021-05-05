"""Main module."""
from task_manager.taskEndpoints import Endpoints
from flask import Flask


app = Flask(__name__)
app.app_context().push()
app.add_url_rule('/api/v1/tasks/db', methods=['POST', 'GET'], view_func=Endpoints.select_insert_db)
app.add_url_rule('/api/v1/tasks/db/<id_db>', methods=['DELETE', 'PUT'], view_func=Endpoints.update_delete_db)


if __name__ == '__main__':
    app.run()
