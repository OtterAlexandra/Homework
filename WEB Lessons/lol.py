db = input()
global_init(db)
db_sess = create_session()
li = db_sess.query(Department).filter(Department.id == 1).members
print(li)

for user in db_sess.query(User).filter(User.id in li, User.):
    print(user.name, user.surname)
