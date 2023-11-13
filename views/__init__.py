from .test_api import info_api

normal_prefix = '/api'
blueprint_prefix = [(info_api, "/info/v1")]

def register_blueprint(app):
    for blueprint, prefix in blueprint_prefix:
        app.register_blueprint(blueprint, url_prefix=normal_prefix+prefix)
    return app