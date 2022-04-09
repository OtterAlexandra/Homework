from flask import Flask

app = Flask(__name__)


@app.route('/')
def hi():
    return '<h1>Hi</h1>'


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>Варианты Выбора</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet_name}</h1>
                        <div class="alert alert-danger" role="alert">
                          Это очень красивая планета
                        </div>
                        
                        <div class="alert alert-warning" role="alert">
                          На ней никого нет, так что вы будете королем 
                        </div>
                        
                        <div class="alert alert-success" role="alert">
                          Также вы сможите обустроить все как вам нравится
                        </div>
                        
                        <div class="alert alert-info" role="alert">
                          Наконец, она просто прикольная!
                        </div>
                        
                      </body>
                    </html>'''


app.run(port=8080, debug=True)
