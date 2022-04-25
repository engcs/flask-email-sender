# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present
"""

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='apps/templates')


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


@app.route('/form', methods=["POST"])
def form():
    title = 'Obrigado!'
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    print(first_name, last_name, email)
    return render_template('form.html', title=title)


if __name__ == '__main__':
    app.run()
