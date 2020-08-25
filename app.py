import os
import sys
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

    @app.route("/")
    def index():
        return jsonify({"status": "Hey I'm working"})

        '''planets'''

    @app.route("/planets")
    @requires_auth('get:planets')
    def get_planets(payload):
        error = False
        try:
            get_planets = Planets.query.all()
            planets = []
            for planet in get_planets:
                planets.append({
                    'id': planet.id,
                    'name': planet.name,
                    'moons_number': planet.moons_number
                })
        except:
            error = True
        finally:
            if error:
                abort(404)
            else:
                return jsonify({
                    'planets': planets
                })

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
            error = True
        finally:
            if error:
                abort(422)
            else:
                return jsonify({
                    'success': True,
                    'name': name,
                    'moons_number': moons_number
                })

    @app.route('/planets/<planet_id>', methods=['DELETE'])
    @requires_auth('delete:planets')
    def del_planets(payload, planet_id):
        error = False
        try:
            planets = Planets.query.filter_by(id=planet_id).first()
            planets.delete()
        except:
            error = True
        finally:
            if error:
                abort(404)
            else:
                return jsonify({
                    'success': True
                })

    @app.route('/planets/<planet_id>', methods=["PATCH"])
    @requires_auth('patch:planets')
    def patch_planets(payload, planet_id):
        error = False
        get_planets = Planets.query.filter_by(id=planet_id).first()
        try:
            name = request.get_json()["name"]
            moons_number = request.get_json()["moonsNumber"]
            get_planets.name = name
            get_planets.moons_number = moons_number
            get_planets.update()
        except:
            error = True
        finally:
            if error:
                abort(422)
            else:
                return jsonify({
                    'success': True
                })

        '''stars'''

    @app.route("/stars")
    @requires_auth('get:stars')
    def stars(payload):
        error = False
        try:
            get_stars = Stars.query.all()
            stars = []
            for star in get_stars:
                stars.append({
                    'id': star.id,
                    'name': star.name,
                    'age': star.age
                })
        except:
            error = True
        finally:
            if error:
                abort(404)
            else:
                return jsonify({
                    'stars': stars})

    @app.route("/stars", methods=["POST"])
    @requires_auth('post:stars')
    def add_stars(payload):
        error = False
        try:
            name = request.get_json()['name']
            age = request.get_json()['age']
            add = Stars(
                name=name,
                age=age
            )
            add.insert()
        except:
            error = True
        finally:
            if error:
                abort(422)
            else:
                return jsonify({
                    'success': True,
                    'name': name,
                    'age': age
                })

    @app.route('/stars/<star_id>', methods=['DELETE'])
    @requires_auth('delete:stars')
    def del_stars(payload, star_id):
        error = False
        stars = Stars.query.filter_by(id=star_id).first()
        try:
            stars.delete()
        except:
            error = True
        finally:
            if error:
                abort(404)
            else:
                return jsonify({
                    'success': True
                })

    @app.route('/stars/<star_id>', methods=['PATCH'])
    @requires_auth('patch:stars')
    def patch_stars(payload, star_id):
        error = False
        try:
            get_stars = Stars.query.filter_by(id=star_id).first()
            name = request.get_json()["name"]
            age = request.get_json()["age"]
            get_stars.name = name
            get_stars.age = age
            get_stars.update()
        except:
            error = True
        finally:
            if error:
                abort(422)
            else:
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

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app


app = create_app()
