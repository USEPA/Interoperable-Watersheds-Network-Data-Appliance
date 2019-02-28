import jwt
import logging
from functools import wraps
from flask import request
from utils.exception import ErrorResponse

JWT_SECRET = ''
JWT_ALGORITHM = 'HS256'
PREFIX = 'Bearer'


def token_required(f):
    @wraps(f)
    def decorated( *args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            raise ErrorResponse('Authorization required to access this resource', 401)
        cleantoken = get_token(token)
        decodedToken = jwt.decode(cleantoken,JWT_SECRET,options={'verify_aud':False})
        logging.info('User access '+decodedToken['user_name'])
        #make sure user has atleast one authority.
        if not decodedToken['authorities'][0]:
            raise ErrorResponse('Authorization required to access this resource', 401)
        return f(*args, **kwargs)
    
    return decorated

def get_token(header):
    bearer, _, token = header.partition(' ')
    if bearer != PREFIX:
        raise ErrorResponse('Token Authorization failed. Invalid Token',401, token)
    return token
