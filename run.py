# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present
"""
# Python core
import os
import smtplib
from datetime import datetime
from typing import Optional
import json

# 3d-party
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
)
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

    @validator('name', allow_reuse=True)
    def validate_valor(cls, v, field):
        if v == 'teste':
            raise RuntimeError(f'{field.name} must between 1 and 10')
        return v


app = Flask(
    __name__, template_folder='apps/templates', static_folder='apps/static'
)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.engine = create_engine('sqlite:///subs.db')
# SQLModel.metadata.create_all(app.engine)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    names = ['Python', 'Software', 'Hardware']
    return render_template('about.html', names=names)


@app.route('/signing', methods=['POST'])
def signing():

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
            print(f'All: {subscribers}')
            flash(f'Registro criado com sucesso!', 'success')
            return redirect('/subscribers')
    except Exception as e:
        print(f'<<Exception>>: {e}')
        return 'There was a error adding your subs...'


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id: int):

    try:
        with Session(app.engine) as db_session:
            statement = select(Subscribers).where(Subscribers.id == id)
            results = db_session.exec(statement)
            subscriber = results.one()
            db_session.delete(subscriber)
            db_session.commit()
    except:
        return 'There was a error deleting your subs...'

    return redirect('/subscribers')


@app.route('/update-form/<int:id>', methods=['GET'])
def update_form(id: int):

    with Session(app.engine) as session:
        statement = select(Subscribers).where(Subscribers.id == id)
        results = session.exec(statement)
        subscriber = results.one()

    return render_template('update-form.html', subscriber=subscriber)


@app.route('/modal/<int:id>')
def registro_pelo_id(id):

    with Session(app.engine) as session:
        sql = select(Subscribers)
        subscribers = session.exec(sql).fetchall()
        return render_template('modal.html', subscribers=subscribers, id=id)


@app.route('/update/<int:id>', methods=['POST'])
def update(id: int):

    print(request.form.get('_method'))
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    with Session(app.engine) as db_session:
        statement = select(Subscribers).where(Subscribers.id == id)
        results = db_session.exec(statement)
        subscriber = results.one()
        subscriber.name = first_name
        subscriber.last_name = last_name
        subscriber.email = email
        db_session.add(subscriber)
        db_session.commit()
        db_session.refresh(subscriber)
        print('Updated subscriber:', subscriber)
        flash(f'Registro atualizado com sucesso!', 'success')

    return redirect('/subscribers')


@app.route('/subscribers', methods=['GET'])
def subscribers():
    with Session(app.engine) as db_session:
        sql = select(Subscribers)
        subscribers = db_session.exec(sql).fetchall()
        return render_template(
            'subscribers.html', subscribers=subscribers)


if __name__ == '__main__':
    app.run(debug=True)
