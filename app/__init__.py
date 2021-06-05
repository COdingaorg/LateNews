from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

#initializing app
app = Flask(__name__, instance_relative_config=True)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing bootstrap
bootstrap = Bootstrap(app)

from app import views
from app import errors