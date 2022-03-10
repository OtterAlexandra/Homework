from flask import Blueprint, jsonify, make_response
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


@jobs_api.route('/api/jobs/<int:job_id>')
def get_job(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)

    if not job:
        return jsonify(
            {
                'error': 'Job not found!'
            }
        )
    return jsonify(
        {
            'jobs': job.to_dict()
        }
    )
