from flask import render_template, flash, redirect
from app import app
from forms import ContactForm

# index
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
		description = 'zapotech // a digital development agency - based in albion, new york',
		page = 'index')

#about
@app.route('/about')
def about():
	return render_template('about.html',
		title = 'about',
		page = 'about')

#work
@app.route('/work')
def work():
	return render_template('work.html',
		title = 'work',
		page = 'work')

#contact
@app.route('/contact', methods=('GET','POST'))
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		return redirect('/')
	return render_template('contact.html',
		title = 'contact',
		page = 'contact',
		form = form)

# 404
@app.errorhandler(404)
def internal_error(error):
  return render_template('404.html',
  	title='404',
  	page='404'), 404

# 500
@app.errorhandler(500)
def internal_error(error):
	return render_template('500.html',
		title='500',
		page='500'), 500