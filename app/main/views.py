from flask import render_template, request, redirect, url_for, flash
from . import main
from .forms import URLForm
from .. import db
from ..models import URLs
from .base import encode, decode
from .errors import page_not_found
import base64

@main.route('/', methods=['GET', 'POST'])
def index():
	url = None
	form = URLForm()
	if form.validate_on_submit():
		url = form.name.data
		#print url
		form.name.data = ''
		if url is not None:
			Url = URLs(url = url)
			db.session.add(Url)
			db.session.commit()
			flash('URL has been added.')
			code = encode(Url.id)
			print Url.id, Url.url
		return redirect(url_for('.added', code = base64.b64encode(code)))#use .name in url_for for blueprint apps
	return render_template('index.html', ip=request.remote_addr, form = form)

@main.route('/shorturl')
def added():
	#base64 encoding to through off dtabase transversal
	return render_template('added.html', url = (url_for('.index', _external=True)+base64.b64decode(request.args.get('code'))))

@main.route('/<code>')
def shorturl(code):
	url = URLs.query.get(decode(code))
	if url is None:
		return render_template('404.html'), 404
	return redirect(url)

