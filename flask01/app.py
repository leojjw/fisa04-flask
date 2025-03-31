# test/__init__.py 변경

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import config

naming_convention = {
     "ix": 'ix_%(column_0_label)s',
     "uq": "uq_%(table_name)s_%(column_0_name)s",
     "ck": "ck_%(table_name)s_%(column_0_name)s",
     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
     "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def create_app():
     app = Flask(__name__)
     app.config.from_object(config)
     # app.config['SQLALCHEMY_ECHO'] = True  # 디버깅용 설정

     db.init_app(app)
     # migrate.init_app(app, db)

     if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
         migrate.init_app(app, db, render_as_batch=True)
     else:
         migrate.init_app(app, db)
 

    # 커스텀 진자 필터 등록
     from filters import format_datetime, format_datetime2
     app.jinja_env.filters['date_time'] = format_datetime
     app.jinja_env.filters['date_time2'] = format_datetime2
 
     from board.views import main_view, board_view, answer_view, auth_view
     app.register_blueprint(main_view.mbp)
     app.register_blueprint(board_view.cbp)
     app.register_blueprint(answer_view.abp)
     app.register_blueprint(auth_view.auth)
    
     return app