from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def hi():
    return '<h1>Hi</h1>'


@app.route('/load_photo')
def load():
    if request.method == 'GET':
        return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_3.css')}" />
                                    <title>Отбор астронавтов</title>
                                  </head>

                                  <body>
                                    <h1>Загрузка фотографии
                                    для участия в миссии</h1>
                                    <div>
                                        <form class="login_form" method="post" enctype="multipart/form-data>
                                            <div class="form-group">
                                                <label for="photo">Приложите фотографию</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                                <p><button type="submit" class="btn btn-primary">Записаться</button></p>
                                            </div>

                                        </form>
                                    </div>
                                  </body>
                                </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        print(f.read())
        return "Форма отправлена"


app.run(port=8080, debug=True)
