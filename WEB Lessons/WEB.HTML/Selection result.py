from flask import Flask

app = Flask(__name__)


@app.route('/')
def hi():
    return '<h1>Hi</h1>'


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                           href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                           integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                           crossorigin="anonymous">
                            <title>Результаты</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            
                            <div class="alert alert-info" role="alert">
                              Претендента на учатие в миссии {nickname}:
                            </div>
                            
                            <div class="alert alert-warning" role="alert">
                              Поздравляем тебя с окончанием {level} этапа.
                            </div>

                            <div class="alert alert-success" role="alert">
                              Ваш рейтинг составляет {rating}!
                            </div>
                            
                            <div class="alert alert-primary" role="alert">
                              Желаем удачи в будущем!
                            </div>

                          </body>
                        </html>'''


app.run(port=8080, debug=True)
