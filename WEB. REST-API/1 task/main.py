from flask import Flask
from jobs_api import jobs_api
from orm import db_session

app = Flask(__name__)
app.register_blueprint(jobs_api)

db_session.global_init("db/db.sqlite")


@app.route('/')
def index():
    return 'Main page'


app.run()
