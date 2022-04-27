# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present
"""
import os
import smtplib

from flask import Flask, render_template, request

app = Flask(
    __name__, template_folder='apps/templates', static_folder='apps/static'
)

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
