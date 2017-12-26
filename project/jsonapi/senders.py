# project/api/senders.py

import os
import json
from flask import Blueprint, jsonify, request
from flask import app
from project.api.utils import authenticate, is_admin
from flask import current_app
import requests


senders_blueprint = Blueprint('senders', __name__)


@senders_blueprint.route('/settings/senders', methods=['GET'])
#@authenticate
def get_all_senders():
    """Get all senders"""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-API-KEY': 'secret'
    }
    url = os.environ.get('CRM_API_ROOT') + '/accounts/2153055/senders.json'
    try:
        response = requests.get(
            url,
            headers=headers
        )
        senders_list = response.json()

        return jsonify({
            'status': 'success',
            'data': {
                'senders': senders_list
            }
        })
    except Exception as e:
        print(e)
        response_object = {
            'status': 'error'
        }
        return response_object, 401
