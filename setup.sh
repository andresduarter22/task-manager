#packaging
python3 -m pip install --upgrade build
python3 -m build
# creates dist/example_pkg-0.0.1-py3-none-any.whl
#test
tox -vvv .
