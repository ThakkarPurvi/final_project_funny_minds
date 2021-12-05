from application import app
from application.routes import backend_host
from flask import url_for
from flask_testing import TestCase
import requests_mock

test_data = {
    "id": 1,
    "name": "Test YoungMind 1",
    "jokes": [
        {
            "id": 1,
            "joke_category": "Festive Jokes",
            "joke_description": "Tring to test jokes",
            "young_mind_id": 1
        }
    ]
}

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

class TestViews(TestBase):

    def test_home_get(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/get/allyoungminds", json={'youngminds': []})
            response = self.client.get(url_for('home'))
            self.assert200(response)

    def test_home_create_youngmind(self):
        response = self.client.get(url_for('create_YoungMind'))
        self.assert200(response)

class TestHome(TestBase):

    def test_home_read_youngminds(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/get/allYoung_Minds", json={'Young_Minds': [test_data]})
            response = self.client.get(url_for('home'))
            self.assertIn("Test Young_Mind 1", response.data.decode("utf-8"))
    
class TestCreateYoung_Mind(TestBase):

    def test_create_Young_Mind_form_post(self):
        with requests_mock.Mocker() as m:
            m.post(f"http://{backend_host}/create/youngmind", text="Test response")
            m.get(f"http://{backend_host}/get/allyoungminds", json={'youngminds': [test_data]})
            response = self.client.post(url_for('create_youngmind'), follow_redirects=True)
            self.assertIn("Test YoungMind 1", response.data.decode("utf-8"))

class TestCreateJoke(TestBase):

    def test_create_joke_form_post(self):
        with requests_mock.Mocker() as m:
            m.post(f"http://{backend_host}/create/joke/1", text="Test response")
            m.get(f"http://{backend_host}/get/allyoungminds", json={'youngminds': [test_data]})
            response = self.client.post(url_for('create_joke'), follow_redirects=True), json={"youngmind": 1, "joke_category": "Test Joke 2"}
            self.assertIn("Test YoungMind 1", response.data.decode("utf-8"))