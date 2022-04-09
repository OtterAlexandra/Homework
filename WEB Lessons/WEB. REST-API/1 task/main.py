from flask import Flask, make_response, jsonify
from jobs_api import jobs_api
from orm import db_session

app = Flask(__name__)
app.register_blueprint(jobs_api)

db_session.global_init("db/db.sqlite")


@app.route('/')
def index():
    return 'Main page'


@jobs_api.errorhandler(404)
def error_404(error):
    return make_response(jsonify({
        'error': 'Jobs not found!'
    }), 404)


app.run()
