from flask_restful import reqparse, abort, Api, Resource
from flask import Flask
from orm import db_session


db_session.global_init('db/new_db.sqlite')
app = Flask(__name__)
