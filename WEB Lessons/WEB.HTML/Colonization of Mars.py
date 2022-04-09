from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return '<h1>Миссия Колонизация Марса</h>'


@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!</h>'


app.run(port=8080, debug=True)
