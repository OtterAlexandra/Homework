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


@app.route('/image_mars')
def image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/image_of_mars.jpg">
                    </br>Вот она, хорошая фотка марса
                  </body>
                </html>'''


app.run(port=8080, debug=True)
