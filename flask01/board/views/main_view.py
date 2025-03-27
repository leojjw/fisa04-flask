from flask import Blueprint, render_template

mbp = Blueprint('main', __name__, url_prefix='/')

@mbp.route('/')
def hello():
    return render_template('index.html')

# @mbp.route('/<username>')
# def print_string(username):
#     return f'{__name__} {username} hello'

# @mbp.route('/path/<path:subpath>')
# def print_path(subpath):
#     return f'{__name__} {subpath} hello'

# @mbp.route('/상품명/')
# @mbp.route('/items/')
# @mbp.route('/items/<itemname>')
# def print_itemname(itemname='기본값'):
#     return f'{__name__} {itemname} hello'