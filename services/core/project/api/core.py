from flask import Blueprint
import json

bp_core = Blueprint('core', __name__)

@bp_core.route('/ping')
def ping():
    response = {'message': 'pong',
                'status': 'success'}
    return json.dumps(response)
