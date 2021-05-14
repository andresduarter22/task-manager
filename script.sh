#!/bin/bash
sudo apt install python3-pip
sudo apt install python3-venv
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt -y install mongodb-org

DIR="./venv"
if [ ! -d "$DIR" ]; then
  python3 -m venv venv
fi
source ./venv/bin/activate
export PYTHONPATH="$(pwd)"
pip3 install -r requirements.txt
./venv/bin/python3 -m build
./venv/bin/python3 tests/test_db_task.py
./venv/bin/python3 task_manager/app.py
