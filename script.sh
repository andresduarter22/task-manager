#!/bin/bash
source ./venv/bin/activate
export PYTHONPATH="$(pwd)"
./venv/bin/python tests/test_db_task.py
./venv/bin/python -m build
./venv/bin/python task_manager/app.py
