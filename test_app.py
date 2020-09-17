import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import random

from app import app, db
from datetime import datetime



class PromoTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.database_name = "promodbtest"
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.app = app.test_client()

        # # binds the app to the current context
        # with self.app.app_context():
        #     self.db = SQLAlchemy()
        #     self.db.init_app(self.app)
        #     # create all tables
        #     self.db.create_all()
        

    def tearDown(self):
        """Executed after reach test"""
        # delete the entries from test db
        models.Users.query.delete()
    
    # questions get
    def test_winner_logic(self):
        rand_chars = [chr(x) for x in range(65, 91)]
        email_gen = [random.choice(rand_chars) + random.choice(rand_chars) for x in range(26)]

        for i in range(26):
            new_email = random.choice(email_gen) + '@mail.com'
            new_code = dict(
                first='Test',
                last='case',
                email= new_email,
                promo_code='ZVLJCYTG')

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
