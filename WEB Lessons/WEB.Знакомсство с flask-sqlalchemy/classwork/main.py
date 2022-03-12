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

user3 = User()
user3.surname = 'Niki'
user3.name = 'Forbs'
user3.age = 20
user3.position = 'system administrator'
user3.speciality = 'head of the management department'
user3.address = 'module_3'
user3.email = 'mister_admini@mars.org'

job = Jobs()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.is_finished = False

db_sess = db_session.create_session()
db_sess.add(user)
db_sess.add(user1)
db_sess.add(user2)
db_sess.add(user3)
db_sess.add(job)
db_sess.commit()
# app.run()
