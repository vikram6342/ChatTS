from flask import Flask
import os


def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        DATABASE = os.path.join(app.instance_path, "Database.sqlite"),
        SECRET_KEY = "dev",
        PERMANENT_SESSION_LIFETIME = 5000,
    )
    if test_config is not None:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass



    from . import db
    db.init_app(app)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)


    
    @app.route("/")
    def home():
        return "", 200


    return app