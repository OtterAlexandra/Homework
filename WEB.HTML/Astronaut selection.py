from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
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
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_2.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>

                          <body>
                            <h1>Анкета претендента</h1>
                            на участие в миссии
                            <div>
                                <form class="login_form" method="post">
                                    <p><input maxlength="30" name="surname" 'value="Введите фамилию"></p>
                                    <p><input maxlength="30" name="name" value="Введите имя"></p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>начальное</option>
                                          <option>среднее</option>
                                          <option>высшее</option>
                                        </select>
                                     </div>

                                    <div>
                                       <p>В каких годах произошли самые известные извержения вулкана Кракатау?</p>
                                       <p><input type="checkbox" name="profession" value="инженер-исследователь"> инженер-исследователь</p>
                                       <p><input type="checkbox" name="profession" value="пилот"> пилот</p>
                                       <p><input type="checkbox" name="profession" value="строитель"> строитель</p>
                                       <p><input type="checkbox" name="profession" value="экзобиолог"> экзобиолог</p>
                                       <p><input type="checkbox" name="profession" value="врач"> врач</p>
                                       <p><input type="checkbox" name="profession" value="инженер по терраформированию"> инженер по терраформированию</p>
                                       <p><input type="checkbox" name="profession" value="климатолог"> климатолог</p>
                                       <p><input type="checkbox" name="profession" value="специалист по радиационной защите"> специалист по радиационной защите</p>
                                       <p><input type="checkbox" name="profession" value="астрогеолог"> астрогеолог</p>
                                       <p><input type="checkbox" name="profession" value="гляциолог"> гляциолог</p>
                                       <p><input type="checkbox" name="profession" value="инженер жизнеобеспечения"> инженер жизнеобеспечения</p>
                                      <div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="4" name="about"></textarea>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


app.run(port=8080, debug=True)
