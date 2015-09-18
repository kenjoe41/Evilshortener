import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'km/Uap"Rj=Q+QO)bmX"q3<lB7'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		#'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
		'mysql://username:password@localhost/db_name'

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		#'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
		'mysql://username:password@localhost/db_name'

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		#'sqlite:///' + os.path.join(basedir, 'data.sqlite')
		'mysql://username:password@localhost/db_name'

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}
