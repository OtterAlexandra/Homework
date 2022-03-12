from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
db_session.global_init("db/mars.db")

user = User()
user.surname = 'Scott'
user.name = 'Ridley'
user.age = 21
user.position = 'captain'
user.speciality = 'research engineer'
user.address = 'module_1'
user.email = 'scott_chief@mars.org'

user1 = User()
user1.surname = 'Middy'
user1.name = 'Cuper'
user1.age = 24
user1.position = 'main engineer'
user1.speciality = 'engineer'
user1.address = 'module_1'
user1.email = 'middy_cuper@mars.org'

user2 = User()
user2.surname = 'Mike'
user2.name = 'Kors'
user2.age = 28
user2.position = 'doctor of main hull'
user2.speciality = 'doctor-surgeon'
user2.address = 'module_2'
user2.email = 'doc_for_you@mars.org'

db_sess = db_session.create_session()
db_sess.add(user)
db_sess.add(user1)
db_sess.add(user2)
db_sess.commit()
# app.run()
