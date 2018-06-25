export PYTHONPATH=$PWD/app
pipenv run python -m unittest discover -s app/test -p test_*.py