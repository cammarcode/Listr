from app import app
from flask import Flask, jsonify, render_template, request, session # noqa
from flask import url_for, redirect, abort # noqa
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, SelectMultipleField, TextAreaField, SubmitField, PasswordField # noqa
from wtforms.validators import DataRequired, Length, EqualTo


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "pizza.db") # noqa
app.config['SECRET_KEY'] = os.urandom(24)  # For CSRF protection
db.init_app(app)


import app.models as models # noqa


@app.route('/')
def home():
    return render_template('home.html', logged=False)


@app.route('/test')
def test():
    return render_template('test.html', logged=False)


@app.route('/testSubmit', methods=['POST'])
def testSubmit():
    num = request.form.get('tomult')
    text = request.form.get('testinp')
    if len(text) <= 50 and int(num) <= 100:  # type: ignore
        print(text * int(num))  # type: ignore
    return render_template('test.html', logged=False, variable=(text * int(num)))  # type: ignore # noqa


@app.route('/login')
def login():
    return render_template('login.html', logged=False)


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('home'))


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)]) # noqa
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)]) # noqa
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # Normally you'd add the user to the database here
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
