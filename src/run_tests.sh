export PYTHONPATH=$PWD/app
pipenv run python -m unittest discover -v -s app/test -p test_*.py