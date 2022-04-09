from flask import Blueprint, jsonify, make_response, request
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


@jobs_api.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})

    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})

    elif request.json['id'] in Jobs.query(Jobs.id).distinct():  # проверка на id
        return jsonify({'error': 'Id already exists'})

    db_sess = db_session.create_session()
    jobs = Jobs(
        id=request.json['id'],
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@jobs_api.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_jobs(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@jobs_api.route('/api/jobs/<int:job_id>', methods=['PUT'])
def red_jobs(job_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})

    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})

    elif request.json['id'] in Jobs.query(Jobs.id).distinct():  # проверка на id
        return jsonify({'error': 'Id already exists'})

    db_sess = db_session.create_session()
    jobs = Jobs.query.filter_by(id=job_id)(
        id=job_id,
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    db_sess.commit()
    return jsonify({'success': 'OK'})
