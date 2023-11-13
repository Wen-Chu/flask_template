from flask import Blueprint
from models import test_get

info_api = Blueprint("info_api", __name__)

@info_api.route('/test')
def test():
    data = test_get.test_models_fuc()
    return data