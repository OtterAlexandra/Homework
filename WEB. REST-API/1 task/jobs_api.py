from flask import Blueprint, jsonify
from orm import db_session
from orm.models import Jobs

jobs_api = Blueprint(
    'job_api',
    __name__,
    template_folder='templates'
)


@jobs_api.route('/api/jobs')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify(
        {
            'jobs': [x.to_dict() for x in jobs]
        }
    )
