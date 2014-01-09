from flask.ext.mail import Message
from flask import render_template
from app import mail
from config import CONTACT_EMAIL
from threading import Thread

def send_async_email(msg):
	mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender = sender, recipients = recipients)
	msg.body = text_body
	msg.html = html_body
	thr = Thread(target = send_async_email, args = [msg])
	thr.start()

def contact_email(name, email, message):
	send_email("Contact Form Email",
		email,
		CONTACT_EMAIL[0],
		render_template('contact_email.txt',
			name = name,
			email = email,
			message = message),
		render_template('contact_email.html',
			name = name,
			email = emailm
			message = message))