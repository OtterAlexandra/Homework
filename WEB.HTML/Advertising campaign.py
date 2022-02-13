from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return '<h1>Миссия Колонизация Марса</h>'


@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!</h>'


@app.route('/promotion')
def promo():
    ad = ["<h1>Человечество вырастает из детства.",
          "Человечеству мала одна планета.",
          "Мы сделаем обитаемыми безжизненные пока планеты.",
          "И начнем с Марса!",
          "Присоединяйся!</h>"]
    return '</br>'.join(ad)


app.run(port=8080, debug=True)
