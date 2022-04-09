from data import db_session
from data.users import User

db = input()
db_session.global_init("db/mars.db")
db_sess = db_session.create_session()
for user in db_sess.query(User).all():
    print(user)
