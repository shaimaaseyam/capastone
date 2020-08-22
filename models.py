import os
from sqlalchemy import Column, Float, Integer, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


database_path = "postgres://tislnfhsdsamur:2f431b33af314a9dd229ba7f6770629d45764b3866359049001bb7fd5bacd11c@ec2-3-215-207-12.compute-1.amazonaws.com:5432/d3kctq9vn2id63"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
planets

'''


class Planets (db.Model):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    moons_number = Column(Integer)

    def __init__(self, name, moons_number):
        self.name = name
        self.moons_number = moons_number

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'moons_number': self.moons_number
        }


'''
stars  

'''


class Stars (db.Model):
    __tablename__ = 'stars'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'name': self.name,
            'age': self.age
        }
