import os
from flask import Flask
from dotenv import load_dotenv

from app.database import db
from app.routes import bp as whatsapp_bp

load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://"
        f"{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}"
        f"@{os.environ.get('DB_HOST', 'localhost')}:{os.environ.get('DB_PORT', '3306')}"
        f"/{os.environ['DB_NAME']}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(whatsapp_bp)

    with app.app_context():
        db.create_all()

    return app