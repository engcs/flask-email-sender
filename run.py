# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present
"""
# Python core
import os
import smtplib
from datetime import datetime

# 3d-party
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    __name__, template_folder='apps/templates', static_folder='apps/static'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initizalize the database
db = SQLAlchemy(app)


# Create db model
class Subscribers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a function to return a string when we add something
    def __rep__(self):
        return '<Name %r>' % self.id


subscribers = []


@app.route('/')
def index():
    title = 'Index'
    return render_template('index.html', title=title)


@app.route('/about')
def about():
    title = 'About'
    names = ['Python', 'Software', 'Hardware']
    return render_template('about.html', title=title, names=names)


@app.route('/hello')
def hello_world():
    return render_template('base.html')


@app.route('/subscribe')
def subscribe():
    title = 'Subscribe'
    return render_template('subscribe.html', title=title)


@app.route('/subscribers', methods=['GET', 'POST'])
def subscribers():
    title = 'Subscribers'
    if request.method == 'POST':
        subs_name = request.form['name']
        new_subs = Subscribers(name=subs_name)
        # Push to database
        try:
            db.session.add(new_subs)
            db.session.commit()
            return redirect('/subscribers')
        except:
            return 'There was a error adding your subs...'
    else:
        subs = Subscribers.query.order_by(Subscribers.date_created)
        return render_template('subscribers.html', title=title, subs=subs)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    title = 'Update'
    sub_to_update = Subscribers.query.get_or_404(id)
    if request.method == 'POST':
        sub_to_update.name = request.form['name']
        try:
            db.session.commit()
            return redirect('/subscribers')
        except:
            return 'There was a problem updating that sub...'
    else:
        return render_template(
            'update.html', title=title, sub_to_update=sub_to_update
        )


@app.route('/form', methods=['POST'])
def form():
    title = 'Obrigado!'
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    message = 'Voce foi inscrito!'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.getenv('MY_EMAIL'), os.getenv('EMAIL_PASSWORD'))
    server.sendmail(os.getenv('MY_EMAIL'), email, message)

    if not first_name or not last_name or not email:
        error_statment = 'Todos os capos são necessários...'
        return render_template(
            'fail.html',
            title=title,
            first_name=first_name,
            last_name=last_name,
            email=email,
            error_statment=error_statment,
        )

    subscribers.append(f'{first_name} {last_name} | {email}')
    return render_template('form.html', title=title, subscribers=subscribers)


if __name__ == '__main__':
    app.run()
