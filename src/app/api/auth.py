from functools import wraps
from flask import request
from utils.exception import ErrorResponse
def token_required(f):
    @wraps(f)
    def decorated( *args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            raise ErrorResponse('Authorization required to access this resource', 401)
        
        if token is not 'secret':
            raise ErrorResponse('Token Authorization failed. Invalid Token',401, token)

        return f(*args, **kwargs)
    
    return decorated