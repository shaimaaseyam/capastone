import os
from models import db, setup_db, Planets, Stars
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route("/planets")
    @requires_auth('get:planets')
    def get_planets(payload):
        error = False
        try:
            get_planets = Planets.query.all()
            planets = []
            for q in get_planets:
                planets.append({
                    'id': q.id,
                    'name': q.name,
                    'moons_number': q.moons_number
                })
        except:
            abort(400)
        finally:
            db.session.close()
        return jsonify({
            'success': True,
            'planets': planets})

    @app.route("/stars")
    @requires_auth('get:stars')
    def stars(payload):
        get_stars = Stars.query.all()
        stars = []
        for q in get_stars:
            stars.append({
                'id': q.id,
                'name': q.name,
                'age': q.age
            })

        return jsonify({
            'stars': stars})

    @app.route("/planets", methods=["POST"])
    @requires_auth('post:planets')
    def add_planet(payload):
        error = False
        try:
            name = request.get_json()['name']
            moons_number = request.get_json()['moonsNumber']
            add = Planets(
                name=name,
                moons_number=moons_number
            )
            add.insert()
        except:
            abort(422)
        finally:
            db.session.close()
        return jsonify({
            'name': name,
            'moons_number': moons_number
        })

    @app.route("/stars", methods=["POST"])
    @requires_auth('post:stars')
    def add_stars(payload):
        name = request.get_json()['name']
        age = request.get_json()['age']
        add = Stars(
            name=name,
            age=age
        )
        add.insert()
        return jsonify({
            'name': name,
            'age': age
        })

    @app.route('/planets/<int:id>', methods=['DELETE'])
    @requires_auth('delete:planets')
    def del_planets(payload, id):
        error = False
        try:
            planets = Planets.query.filter_by(id=id).first()
            planets.delete()
        except:
            abort(404)
        return jsonify({
            'success': True
        })

    @app.route('/stars/<int:id>', methods=['DELETE'])
    @requires_auth('delete:stars')
    def del_stars(payload, id):
        error = False
        try:
            stars = Stars.query.filter_by(id=id).delete()
        except:
            abort(404)
        return jsonify({
            'success': True
        })

    @app.route('/stars/<int:id>', methods=['PATCH'])
    @requires_auth('patch:stars')
    def patch_stars(payload, id):
        name = request.get_json()["name"]
        age = request.get_json()["age"]
        get_stars = Stars.query.filter_by(id=id).first()
        get_stars.name = name
        get_stars.age = age
        get_stars.update()
        return jsonify({
            'success': True
        })

    @app.route('/planets/<int:id>', methods=['PATCH'])
    @requires_auth('patch:planets')
    def patch_planets(payload, id):
        name = request.get_json()["name"]
        moons_number = request.get_json()["moonsNumber"]
        get_planets = Planets.query.filter_by(id=id).first()
        get_planets.name = name
        get_planets.moons_number = moons_number
        get_planets.update()
        return jsonify({
            'success': True
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": " Internal Server Error"
        }), 500
    return app


app = create_app()
