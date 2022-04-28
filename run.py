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
from flask_sqlalchemy import SQLAlchemy
from sqlmodel import Field, SQLModel, Session, create_engine, select
from pydantic import validator


class Subscribers(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    date_created: datetime = Field(
        default_factory=datetime.utcnow, nullable=False
    )


app = Flask(
    __name__, template_folder='apps/templates', static_folder='apps/static'
)
app.engine = create_engine('sqlite:///subs.db')


@app.route("/", methods=["GET", "POST"])
def create_post():
    # if request.method == "POST":
    #     name = request.form.get("name")
    #     with Session(app.engine) as session:
    #         session.add(Subscribers(name=name))
    #         session.commit()
    # return render_template("subscribers.html")
    with Session(app.engine) as session:
        sql = select(Subscribers)
        subscribers = session.exec(sql).fetchall()
    return str(subscribers)


if __name__ == '__main__':
    app.run(debug=True)
