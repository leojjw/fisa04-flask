# test/__init__.py 변경

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
     app = Flask(__name__)
     app.config.from_object(config)

     db.init_app(app)
     migrate.init_app(app, db)

     from views import main_view, board_view
     app.register_blueprint(main_view.mbp)
     app.register_blueprint(board_view.cbp)
    
     return app