from flask_restx import Namespace, fields


class UserDto:
    user_api = Namespace('user', description='user related operations')
    user = user_api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })


class AuthDto:
    auth_api = Namespace('auth', description='authentication related operations')
    user_auth = auth_api.model('auth_details', {
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password '),
    })


class TasksDto:
    tasks_api = Namespace('tasks', description='TODO operations')
    todos = tasks_api.model('tasks_details', {
        'id': fields.Integer(readonly=True, description='The task unique identifier'),
        'task': fields.String(required=True, description='The task details')
    })

