import unittest
from app import create_app, db
from app.models import Subscriber

class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_success_page(self):
        response = self.client.get('/success')
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_page_not_found(self):
        response = self.client.get('/page-not-exist')
        self.assertEqual(response.status_code, 404)

    def test_new_subscriber(self):
        response = self.client.post('/', data={
            'email': 'newsubscriber@example.com'})
        self.assertEqual(response.status_code, 302)

    def test_same_subscriber(self):
        s = Subscriber(email='alreadyregistered@example.com')
        db.session.add(s)
        db.session.commit()
        response = self.client.post('/', follow_redirects=True,
                data={'email': 'alreadyregistered@example.com'})
        self.assertTrue('Este email já está registrado!' in
                response.get_data(as_text=True))

    def test_new_message(self):
        response = self.client.post('/contact', data={
            'firstname': 'example',
            'lastname': 'example',
            'subject': 'Outro',
            'email': 'newmessage@example.com',
            'body': 'A new message!'})
        self.assertEqual(response.status_code, 302)
