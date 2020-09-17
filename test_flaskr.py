import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import random

from flaskr import create_app
from models import setup_db, Question, Category
from datetime import datetime
import random


class PromoTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "promodbtest"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        # delete the entries from test db
        models.Users.query.delete()
    
    # questions get
    def test_winner_logic(self):
        email_gen = []
        new_code = dict(
            first='Test',
            last='case',
            email='test@mail.com',
            promo_code='ZVLJCYTG')
        for i in range(26):
            self.client().post('/promo/new', json=new_code)
        outcomes = list(Users.query.filter(won=True).all())

        self.assertNotEqual(len(outcome), 0)

    # sumbit new promotion code
    def test_new_submission(self):
        new_code = dict(
            first='Test',
            last='case',
            email='test@mail.com',
            promo_code='ZVLJCYTG')

        q_len_before = len(Users.query.all())        
        res = self.client().post('/promo/new', json=new_q)
        q_len_after = len(Users.query.all()) 

        self.assertGreaterEqual(q_len_before, q_len_after)

    #TODO need to test flash
    # # Duplicate code
    # def test_duplicate_submission(self):
    #     new_code = dict(
    #         first='Test',
    #         last='case',
    #         email='test@mail.com',
    #         promo_code='ZVLJCYTG')

    #     res = self.client().post('/promo/new', json=new_code)

    #     self.assertEqual()


    # # Test invalid promotion code
    # def test_invalid_code(self):
    #     code = 'DEADBEEF'
    #     res = self.client().post('/promo/new', json=new_code)

    #     self.assertEqual()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
