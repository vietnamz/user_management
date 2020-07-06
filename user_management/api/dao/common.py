from flask_restplus import fields
from api import api

"""
Common error message and data.
"""
error = api.model('Error', {
    'code': fields.String(example='USR_02'),
    'message': fields.String(example='Endpoint not found.'),
    'field': fields.String(example='The field example is empty.'),
    'status': fields.String(example='500')
})

unauthorized = api.model('Unauthorized', {
    'code': fields.String(example='AUT_02'),
    'message': fields.String(example='The Api key is invalid.'),
    'field': fields.String(example='API-KEY')
})

notfound = api.model('NotFound', {
    'message': fields.String(example='Endpoint not found.'),
})