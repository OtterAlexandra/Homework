from flask import Flask, request, url_for

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
                    <img src="static/img/image_of_mars.jpg" />
                    </br>Вот она, хорошая фотка марса
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_with_photo():
    # ad = ["<h2>Человечество вырастает из детства.",
    #      "Человечеству мала одна планета.",
    #      "Мы сделаем обитаемыми безжизненные пока планеты.",
    #      "И начнем с Марса!",
    #      "Присоединяйся!</h2>"]
    # ad = '</br>'.join(ad)

    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/img/image_of_mars.jpg" />
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


app.run(port=8080, debug=True)

# скачать bootstrap и доделать promotion_with_photo
