import os
from flask import Flask, render_template, request, redirect, send_file, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from db import *

app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'Павел'
app.config['MAIL_PASSWORD'] = '30eaapwbjkl'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


def send_email(subject, body):
    recipients = Email.query.all()  
    
    for recipient in recipients:
        msg = Message(subject, recipients=[recipient.email])
        msg.body = 'This is a test email.'
        mail.send(msg)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/our_projects')
def our_projects():
  return render_template('our_projects.html')


@app.route('/services')
def services():
  return render_template('services.html')


@app.route('/add_email', methods=['POST'])
def add_email():
    email = request.form['email']
    
    new_email = Email(email=email)
    db.session.add(new_email)
    db.session.commit()
    
    return render_template('index.html')  


if __name__ == "__main__":
  app.run(debug=True)