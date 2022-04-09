from flask import Flask
from .data import db_session
from .data.users import User
from .data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/blogs.db")

user = User()
user.name = "Пользователь 1"
user.about = "биография пользователя 1"
user.email = "email@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()
user = db_sess.query(User).first()

news = News(title="Первая новость", content="Привет блог!",
            user_id=1, is_private=False)
db_sess.add(news)
db_sess.commit()

user1 = db_sess.query(User).filter(User.id == 1).first()
news = News(title="Вторая новость", content="Уже вторая запись!",
            user=user1, is_private=False)
db_sess.add(news)
db_sess.commit()

# app.run()
