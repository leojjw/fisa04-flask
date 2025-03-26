from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return f'Hello, {__name__}'

if __name__ == '__main__':
    app.run(debug=True, port=5001)