from flask import render_template
from app import app

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
@app.route('/contact')
def contact():
	return render_template('contact.html',
		title = 'contact',
		page = 'contact')