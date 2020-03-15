from flask import Flask
import os

def config_blueprint(flask_app):
    from app.views import task
    flask_app.register_blueprint(task)

def config_extension(flask_app):
    from app.ext import db
    db.init_app(flask_app)

def config_settings(flask_app):
    cfg = "app.config.{env}Config"
    app_env = os.environ.get("FLASK_ENV", "development")
    flask_app.config.from_object(cfg.format(env=app_env.capitalize()))

def create_app():
    flask_app = Flask(__name__)
    config_settings(flask_app)
    config_blueprint(flask_app)
    config_extension(flask_app)
    return flask_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")