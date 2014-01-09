from flask.ext.mail import Message
from flask import render_template
from app import mail
from config import CONTACT_EMAIL

def send_email(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender = sender, recipients = recipients)
	msg.body = text_body
	msg.html = html_body
	mail.send(msg)

def contact_email(form_content):
	send_email("Contact Form Email",
		[form_content.email],
		CONTACT_EMAIL[0],
		render_template('contact_email.txt',
			content = form_content),
		render_template('contact_email.html',
			content = form_content))