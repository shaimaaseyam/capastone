import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import app
from models import setup_db, db, Planets, Stars


class GalaxyTestCase(unittest.TestCase):
    """This class represents the galaxy test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_path = os.environ['TEST_DATABASE_URI']
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_422_name(self):
        res = self.client().post(
            '/planets', json={'name': '', 'moonsNumber': ''})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)

    def test_get_planets_by_id(self):
        res = self.client().get('/planet/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_404_sent_deleting_non_existing_planet(self):
        res = self.client().delete('/planets/a')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_planet_with_invalid_id(self):
        res = self.client().delete('/planets/sadsa2112kjsds6')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
