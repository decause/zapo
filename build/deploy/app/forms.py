from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, email

class ContactForm(Form):
	name = TextField('name', validators=[DataRequired()])
	email = EmailField('email', validators=[email()])
	message = TextAreaField('message', validators=[DataRequired()])