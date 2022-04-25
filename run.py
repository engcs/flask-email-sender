# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder="apps/templates")


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello_world():
    return '<p>Hello, World!</p>'


if __name__ == '__main__':
    app.run()
