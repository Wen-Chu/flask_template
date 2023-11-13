from flask import Flask
from flask_cors import CORS
# import models
from views import register_blueprint
from lib import config
# from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)
    app.jinja_env.auto_reload = True
    app.config.from_object(config.Config())
    CORS(app)

    # models.setup(app)

    # register app
    register_blueprint(app)

    # Swagger doc
    # swagger_blueprint = get_swaggerui_blueprint(
    #     '/api/document',
    #     '/static/APIdoc.json',
    #     config={
    #         'app_name': "flask_template"
    #     }
    # )
    # app.register_blueprint(swagger_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port='1113', debug=True, threaded=False)