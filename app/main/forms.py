from wtforms import StringField, SubmitField
from wtforms.validators import Required, URL
from flask.ext.wtf import Form
#from wtforms.fields import TextAreaField

class URLForm(Form):
	name = StringField('Enter URL to shorten:', validators=[Required(), URL(message='Invalid URL. Try adding \'http://\'')])
	submit = SubmitField('Submit')
