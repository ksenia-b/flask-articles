from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
# from data import Articles
from models import *
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_migrate import  MigrateCommand
from flask_script import Manager
from flask_security import SQLAlchemyUserDatastore
from flask import request
import hashlib

app = Flask(__name__)

# postgres config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    article = Article.query.filter(Post.slug == slug).findall()

    return render_template('article.html', article=article)
    # @posts.route('/<slug>')
    # def post_detail(slug):
    #     post = Post.query.filter(Post.slug == slug).first_or_404()
    #     tags = post.tags
    #     return render_template('posts/post_detail.html', post=post)
    #
    # return render_template('article.html', articles = Articles)


@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        user_name = form.username.data
        email = form.email.data
        password = form.password.data

        password = hashlib.md5(str(form.password.data).encode('utf-8'))
        # password = sha256_crypt.encrypt(str(form.password.data))

        try:
            user = User(email=email, user_name=user_name, password=password, register_day="12345", name=name)
            print("article = ", user)
            db.session.add(user)
            print("add user")
            db.session.commit()
            print("comittt")
        except:
            print("Something wrong!")
            print("article = ")

        flash('You are now registered and can log in.', 'success')
        return redirect(url_for('index'))

    return render_template('register.html', form=form)

    # form = PostForm()
    # return render_template('posts/create_post.html', form=form)


if __name__ == '__main__':
    app.secret_key = 'SECRET KEY'
    app.run(debug=True)