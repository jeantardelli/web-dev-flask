import unittest
from app import create_app, db
from app.models import Subscriber

class SubscriberModelTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_subscribe_registration(self):
        s = Subscriber(email='newsubscriber@example.com')
        self.assertTrue(s.email is not None)

    def test_subcribe_sameuser(self):
        s1 = Subscriber(email='newsubscriber@example.com')
        s2 = Subscriber(email='newsubscriber@example.com')
        db.session.add(s1)
        db.session.add(s2)
        with self.assertRaises(Exception):
            db.session.commit()
