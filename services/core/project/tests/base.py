from project import create_app
from project.utils.db import db
from flask_testing import TestCase

app = create_app()


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
