# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present
"""
# Python core
import os
import smtplib
from datetime import datetime
from typing import Optional

# 3d-party
from flask import Flask, redirect, render_template, request
from pydantic import validator
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Subscribers(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    last_name: str
    email: str
    date_created: datetime = Field(
        default_factory=datetime.utcnow, nullable=False
    )

    @validator('name')
    def validate_valor(cls, v, field):
        if v == 'teste':
            raise RuntimeError(f'{field.name} must between 1 and 10')
        return v


app = Flask(
    __name__, template_folder='apps/templates', static_folder='apps/static'
)
app.engine = create_engine('sqlite:///subs.db')
# SQLModel.metadata.create_all(app.engine)


@app.route('/')
def index():
    return redirect('/subscribe')


@app.route('/about')
def about():
    title = 'About'
    names = ['Python', 'Software', 'Hardware']
    return render_template('about.html', names=names)


@app.route('/hello')
def hello_world():
    return render_template('base.html')


@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')


# @app.route('/', methods=['GET', 'POST'])
# def create_post():
#     # if request.method == "POST":
#     #     name = request.form.get("name")
#     #     with Session(app.engine) as session:
#     #         session.add(Subscribers(name=name))
#     #         session.commit()
#     # return render_template("subscribers.html")
#     with Session(app.engine) as session:
#         sql = select(Subscribers)
#         subscribers = session.exec(sql).fetchall()
#     return render_template('subscribers.html', subscribers=subscribers)


@app.route('/signed', methods=['POST'])
def signed():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        try:
            with Session(app.engine) as session:
                new_subscriber = Subscribers(
                    name=first_name, last_name=last_name, email=email
                )
                session.add(new_subscriber)
                session.commit()
                sql = select(Subscribers)
                subscribers = session.exec(sql).fetchall()
                return render_template('signed.html', subscribers=subscribers)
        except Exception as e:
            print(f'<<Exception>>: {e}')
            return 'There was a error adding your subs...'


@app.route('/delete/<int:id>')
def delete(id: int):
    try:
        with Session(app.engine) as session:
            statement = select(Subscribers).where(Subscribers.id == id)
            results = session.exec(statement)
            subscriber = results.one()
            session.delete(subscriber)
            session.commit()
    except:
        return 'There was a error deleting your subs...'
    return redirect('/subscribers')


@app.route('/update_form/<int:id>', methods=['GET'])
def update(id: int):
    with Session(app.engine) as session:
        statement = select(Subscribers).where(Subscribers.id == id)
        results = session.exec(statement)
        subscriber = results.one()

    return render_template('update.html', subscriber=subscriber)


@app.route('/update/<int:id>', methods=['POST'])
def update(id: int):

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    with Session(app.engine) as session:
        statement = select(Subscribers).where(Subscribers.id == id)
        results = session.exec(statement)
        subscriber = results.one()
        subscriber.name = first_name
        subscriber.last_name = last_name
        subscriber.email = email
        session.add(subscriber)
        session.commit()
        session.refresh(subscriber)
        print('Updated subscriber:', subscriber)

    return redirect('/subscribers')


@app.route('/subscribers', methods=['GET'])
def subscribers():
    with Session(app.engine) as session:
        sql = select(Subscribers)
        subscribers = session.exec(sql).fetchall()
        return render_template('subscribers.html', subscribers=subscribers)


if __name__ == '__main__':
    app.run(debug=True)
