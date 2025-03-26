from flask import Blueprint

mbp = Blueprint('main', __name__, url_prefix='/main')

@mbp.route('/')
def hello():
    return f'Hello, {__name__}'

@mbp.route('/<username>')
def print_string(username):
    return f'{__name__} {username} hello'

@mbp.route('/path/<path:subpath>')
def print_path(subpath):
    return f'{__name__} {subpath} hello'
