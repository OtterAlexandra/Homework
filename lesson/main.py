from flask import Flask
from .data import db_session
from .data.models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init('db/blogs.sqlite')

user1 = User()
user1.name = "Пользователь 1"
user1.about = "биография пользователя 1"
user1.email = "email@e.ru"
user2 = User()
user2.name = "Пользователь 2"
user2.about = "биография пользователя 2"
user2.email = "email@em.ru"
user3 = User()
user3.name = "Пользователь 3"
user3.about = "биография пользователя 3"
user3.email = "email@ema.ru"

db_sess = db_session.create_session()
db_sess.add(user1)
db_sess.add(user2)
db_sess.add(user3)
db_sess.commit()


# app.run()
