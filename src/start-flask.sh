export FLASK_APP=app.app:application
export FLASK_ENV=development
export PYTHONPATH=$PWD/app
echo 'PYTHONPATH ='$PYTHONPATH
echo 'FLASK_APP='$FLASK_APP 
echo 'FLASK_ENV='$FLASK_ENV
pipenv run flask run