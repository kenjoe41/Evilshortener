from . import db

class URLs(db.Model):
	__tablename__ = 'urls'
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(2000), unique=False)
	def __init__(self, url):
		self.url = url
	def __repr__(self):
		return '<URL %r>' % self.url

