import datetime
import logging

import jwt
import main

from functools import wraps
from flask import request
from service.auth_service import Auth
from typing import Callable



def encode_auth_token(user_id: int) -> bytes:
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            main.secret_key_,
            algorithm='HS256'
        )
    except Exception as e:
        logging.error("{}-{}".format(encode_auth_token, e))
        return e