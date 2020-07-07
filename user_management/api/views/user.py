from flask_restplus import Resource
from flask import request, jsonify

from api import user_namespace
from api.dao.common import *
from api.dao.user import *
from api.middleware.user import *

"""
View for user management namespace
"""


@user_namespace.route('')
class User(Resource):
    @api.response(500, 'Return a error object.', error)
    @api.marshal_with(user, code=200,
                      description='Return a Object of User.')
    @api.expect(newly_user_data, validate=False)
    @api.doc(body=newly_user_data)
    def post(self):
        """
        Create a newly user
        """
        return register_with_phone(form_data=request.form)

    @api.response(500, "Return an error object", error)
    @api.marshal_with(user, code=200,
                      description='Return a Object of User.')
    @api.expect(query_params1, validate=True)
    @api.doc(body=query_params1)
    def get(self):
        """
        Retrieve a list of user OR Retrive a user base on phone number, user id, email.
        Ex:
        phone=+939717135
        email=delgemoon@gmail.com
        user_id=1
        :return:
        """
        if len( request.args ) > 1:
            raise CustomException('multiple params do not allowed', 400,
                                   {'field': 'URI Params',
                                    'code': 'USR_0'})
        """
        do transformation to make one query is used.
        The priority order is:
        phone: most used
        email: user for validation as example.
        id: database id, rarely used, do not expected to use.
        """
        query = defaultdict()
        """
        phone is a main authorization method.
        so account name is a phone number now.
        ex: +84939717135
        """
        if request.args.get('phone'):
            query['account'] = request.args['phone']
        elif request.args.get('email'):
            query['email'] = request.args['email']
        elif request.args.get('user_id'):
            query['user_id'] = request.args['user_id']
        else:
            print( "unkown query paras get all")
        if len(query) != 0:
            return get_user_profile(**query)
        return get_all_users()


@user_namespace.route('/<string:user_uuid>')
@api.param('user_uuid', 'User UUID')
class UserWithUUID(Resource):
    @api.response(500, 'Return a error object.', error)
    @api.marshal_with(user, code=200,
                      description='Return a Object of User.')
    def get(self, user_uuid):
        """
        Retrieve a specific user information base backend user uuid
        """
        query = defaultdict()
        query['user_uuid'] = user_uuid
        return get_user_profile(**query)  # User UUID attribute

    @api.response(500, 'Return a error object.', error)
    @api.marshal_with(user, code=200,
                      description='Return a Object of User.')
    @api.expect(user_data, validate=True)
    @api.doc(body=user_data)
    def put(self, user_uuid):
        """
        Update a specific user information base backend user uuid
        """
        query = defaultdict()
        query['user_uuid'] = user_uuid
        get_user_profile(**query)
        print ( request.json)
        return update_user(request.json)

    @api.response(500, 'Return a error object.', error)
    @api.response(200, 'Return status object')
    def delete(self, user_uuid):
        """
        Delete a specific user information base backend user uuid
        """
        print(user_uuid)
        delete_user(user_uuid)
        return jsonify({'status': 'OK'})




