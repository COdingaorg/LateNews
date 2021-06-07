from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

#initializing bootstrap
bootstrap = Bootstrap()

#initializing app
def create_app(config_name):
  app = Flask(__name__)

  #Creating app configurations
  app.config.from_object(config_options[config_name])
  app.config.from_pyfile('config.py')

  #initializing flask extensions
  bootstrap.init_app(app)

  from app import views
  from app import errors

  return app

