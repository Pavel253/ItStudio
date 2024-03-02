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
  posts = Post.query.all()
  return render_template('our_projects.html', posts=posts)



@app.route('/services')
def services():
  return render_template('services.html')


@app.route('/forms')
def forms():
  return render_template('forms.html')


@app.route('/upload', methods=['POST'])
def upload():
    name = request.form.get('name')
    
    image = request.files['image']
    image_data = image.read()
    
    new_image = Post(name=name, image=image_data)
    
    db.session.add(new_image)
    db.session.commit()
    
    return 'Image uploaded successfully'


@app.route('/add_email', methods=['POST'])
def add_email():
    email = request.form['email']
    
    new_email = Email(email=email)
    db.session.add(new_email)
    db.session.commit()
    
    return render_template('index.html')
  


if __name__ == "__main__":
  app.run(debug=True)