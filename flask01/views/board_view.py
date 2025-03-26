from flask import Blueprint

cbp = Blueprint('collection', __name__, url_prefix='/board')

@cbp.route('/no1')
def hello2():
    return f'{__name__} 첫번째'
    
@cbp.route('/no2')
def hello3():
    return f'{__name__} 두번째'
    