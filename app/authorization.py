import os

import flask
import requests
import zign.api

TEAMS_URL = os.getenv('TEAMS_URL')


def check_auth(team):
    token = zign.api.get_token('teams', ['uid'])
    if not hasattr(flask.request, 'user') or not TEAMS_URL:
        return True
    response = requests.get(TEAMS_URL, params={'member': flask.request.user},
                            headers={'Authorization': 'Bearer {0:s}'.format(token)})
    return True
