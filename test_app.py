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
        self.human_token = f"Bearer {os.environ['HUMAN_TOKEN']}"
        self.alien_token = f"Bearer {os.environ['ALIEN_TOKEN']}"
        self.human_header = {'Authorization': self.human_token}
        self.alien_header = {'Authorization': self.alien_token}
        self.wrong_headers = {'Authorization': 'edgfpfedogjk'}
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_add_200_planet(self):
        res = self.client().post(
            '/planets', json={'name': 'hulk', 'moonsNumber': '2'}, headers=self.human_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_add_422_planet(self):
        res = self.client().post(
            '/planets', json={'name': 'funny', 'moonsnumber': True}, headers=self.human_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def test_get_planets_by_wrong_route_404(self):
        res = self.client().get('/planet/1', headers=self.human_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_get_planets_200(self):
        res = self.client().get('/planets', headers=self.human_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_200_edit_planets(self):
        res = self.client().patch('/planets/1',
                                  json={'name': 'hulk', 'moonsNumber': 2}, headers=self.human_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_422_edit_planets(self):
        res = self.client().patch(
            '/planets/11111', json={'name': 'sunny', 'moonsNumber': 2}, headers=self.human_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def test_delete_planet_with_invalid_id(self):
        res = self.client().delete('/planets/11111', headers=self.human_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_200_planets_sent_deleting(self):
        res = self.client().delete('/planets/2', headers=self.human_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    # stars tests
    def test_200_add_a_star(self):
        res = self.client().post(
            '/stars', json={'name': '33', 'age': 2}, headers=self.alien_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_add_422_stars(self):
        res = self.client().post(
            '/stars', json={'name': 'funny', 'age': True}, headers=self.alien_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def test_get_stars_by_wrong_route_404(self):
        res = self.client().get('/star', headers=self.alien_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_get_stars_200(self):
        res = self.client().get('/stars', headers=self.alien_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_200_edit_stars(self):
        res = self.client().patch('/stars/2',
                                  json={'name': 'hulk', 'age': 2}, headers=self.alien_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_422_edit_stars(self):
        res = self.client().patch(
            '/stars/11111', json={'name': 'sunny', 'age': 2}, headers=self.alien_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def test_delete_stars_with_invalid_id(self):
        res = self.client().delete('/stars/11111', headers=self.alien_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_200_stars_sent_deleting(self):
        res = self.client().delete('/stars/1', headers=self.alien_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
