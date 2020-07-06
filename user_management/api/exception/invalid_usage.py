"""
custom exception:
Code:

    USER_01: Missing Fields.
    USER_02: Unauthentication,
    USER_03: Db error (  default )
    USER_04: Firebase error.
"""
class CustomException(Exception):
    status_code = '400'

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['code'] = 'USER_03'
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        print(rv)
        return rv
