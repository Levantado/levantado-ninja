from flask import Blueprint, render_template
import json

bp_api_core = Blueprint('api_core', __name__, template_folder='templates')


@bp_api_core.route('/ping')
def ping():
    response = {'message': 'pong',
                'status': 'success'}
    return json.dumps(response)


@bp_api_core.route('/')
def index():
    return render_template('index.html'), 200
