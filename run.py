# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='apps/templates')


@app.route('/')
def index():
    title = 'Index'
    return render_template('index.html', title=title)


@app.route('/about')
def about():
    title = 'About'
    return render_template('index.html', title=title)


@app.route('/hello')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
