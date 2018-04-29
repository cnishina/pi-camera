## Running flask server

Setup virtualenv then activate the virtual environment.

```
virtualenv venv
source venv/bin/activate
```

pip install the requirements file.
```
pip install -r requirements.txt
```

export the environment variable for `FLASK_APP` then run flask.
```
export FLASK_APP=server.py
flask run
```