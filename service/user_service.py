import logging
import uuid

import main
from typing import Dict, Tuple
from util.decorator import encode_auth_token

logging.basicConfig(filename='cc.log', level=logging.DEBUG)


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    # Create variables for easy access
    username = data['username']
    password = data['password']
    email = data['email']
    if int(get_a_user(username)) > 0:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409
    else:
        pwd = main.pwd_salt(password)
        msg = main.insert_data(username, pwd, email)
        if msg == 'You have successfully registered!':
            try:
                # generate the auth token
                random_id = uuid.uuid4()
                auth_token = encode_auth_token(int(random_id))
                response_object = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'Authorization': auth_token
                }
                return response_object, 201
            except Exception as e:
                logging.error(e)
                response_object = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Something went wrong',
            }
            return response_object, 500


def get_a_user(username):
    cursor = main.mysql.connection.cursor(main.MySQLdb.cursors.DictCursor)
    query = 'SELECT * FROM accounts WHERE username = "{0}"'.format(username)
    return cursor.execute(query)
