from flask import Flask
import os

from project.utils.db import db
from project.api.core import bp_api_core


def create_app():
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    db.init_app(app)
    app.register_blueprint(bp_api_core, url_prefix='/')
    return app
