from flask_testing import TestCase
from application import app, db
from flask import url_for
from application.models import YoungMind
from application.models import Joke

test_youngmind = {
                
                "id": 1,
                "name": "YoungMind 1",
                "jokes": []
                
            }
test_joke = {
                "id": 1,
                "joke_category": "Joke 1",
                "joke_description": "Joke 1",
            }

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        # Create table schema
        db.create_all()
        db.session.add(YoungMind(youngmind_name="YoungMind 1"))
        db.session.commit()


    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()


class TestRead(TestBase):
    def test_read_all_youngminds(self):
        response = self.client.get(url_for("read_all_youngminds"))
        all_youngmind = { "youngminds" : [test_youngmind]}
        self.assertEquals(all_youngminds, response.json)

    def test_read_youngminds(self):
        response = self.client.get(url_for("read_youngmind", id = 1))
        json = {"youngmind_name": "YoungMind 1", "id": 1}
        self.assertEquals(json, response.json)

    

class TestCreate(TestBase):
    def test_add_youndmind(self):
        response = self.client.post(
            url_for("add_youngmind"),
            json ={"youngmind_name": "Testing add functionality"},
            follow_redirects=True
        )
        self.assertEquals(b"Added New YoungMind: Testing add functionality", response.data)
       
class TestUpdate(TestBase):
    def test_update_youngmind(self):
        response = self.client.put(
            url_for("update_youngmind", id=1),
            json ={"name": "Testing update functionality"}
        )
        self.assertEquals(b"Updated YoungMind ID: 1 ", response.data)

class TestDelete(TestBase):
    def test_delete_task(self):
        response = self.client.delete(url_for("delete_youngmind", id=1))
        self.assertEquals(b"Deleted YoungMind with ID: 1 ", response.data)
        self.assertIsNone(Country.query.get(1))