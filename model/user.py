import datetime
import jwt
import hashlib
import uuid
import main

from typing import Union


class User:
    id = int(uuid.uuid4())

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.getter
    def password(self, password):
        pass

    @staticmethod
    def get_user(username, pwd):
        pwd_salt = User.check_password(pwd)
        cursor = main.mysql.connection.cursor(main.MySQLdb.cursors.DictCursor)
        query = 'SELECT * FROM accounts WHERE username ="{0}" AND password ="{1}"'.format(username, pwd_salt)
        cursor.execute(query)
        # Fetch one record and return result
        return cursor.fetchone()

    @staticmethod
    def check_password(password: str):
        salt = "G@me"
        db_password = password + salt
        tmp = hashlib.md5(db_password.encode())
        return str(tmp.hexdigest())

    @staticmethod
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
            return e

    @staticmethod
    def decode_auth_token(auth_token: str) -> Union[str, int]:
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, main.secret_key_)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<User '{}'>".format(self.username)
