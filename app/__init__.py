from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from config import config

bootstrap = Bootstrap()
manager = Manager()
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	bootstrap.init_app(app)
	db.init_app(app)

	# attach routes and custom error pages here
	from main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	
	return app

