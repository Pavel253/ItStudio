from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
db = SQLAlchemy(app)

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(300), nullable=False)
  text = db.Column(db.Text, nullable=False)


@app.route('/index')
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


if __name__ == "__main__":
  app.run(debug=True)