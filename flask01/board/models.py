from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=True, server_default="1")
    # user테이블 pk로 작성자를 구분 - nullable=False 로 변경, ondelete='CASCADE'로 변경 
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    # 작성자를 넣을것
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=True, server_default="1")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))  # user를 통해 answer_set 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)