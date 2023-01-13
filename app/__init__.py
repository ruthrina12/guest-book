from flask import Flask
from app.ext import db
from app.models import Record

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///guestbook.db"

    db.init_app(app)

    from .view import main
    app.register_blueprint(main) 
 
    @app.shell_context_processor
    def make_shell_context():
        return {
            'app':app,
            'db':db,
            'Record':Record
        }

    return app