import os
from sqlalchemy import Column, Float, Integer, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


database_path = "postgres://dlfkzynkcrcqzl:0c986cd0507440ce12818cffdf80f4f80e6dd0ea871eff1d4541942e60219383@ec2-34-238-26-109.compute-1.amazonaws.com:5432/dc3o4knthcv81o"

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
