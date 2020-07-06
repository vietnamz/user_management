from api.exception.invalid_usage import CustomException
from collections import defaultdict
from api.dal import Dal
from .common import  _validate_input_form
from uuid import uuid4
from api.services.firebase import get_user_by_phone_number

"""
user validation.
"""


def _createUUID4():
    """
    private method to generate unique uuid
    :return:
    """
    return uuid4()


def update_user(json=None):
    if not json['account']:
        raise CustomException('The user phone is missing', '400', {'field': 'account',
                                                                   'code': 'USR_0'})
    if not json['email']:
        raise CustomException('The user phone is missing', '400', {'field': 'email',
                                                                   'code': 'USR_0'})
    if not json['user_uuid']:
        raise CustomException('The user phone is missing', '400', {'field': 'user_uuid',
                                                                   'code': 'USR_0'})
    query = defaultdict()
    query['account'] = json['account']

    user = Dal.get_user_by(**query)
    user.update(**json)
    user.save()
    return user


def register_with_phone(header=None, form_data=None):
    """ This method is used to perform register for the first user from phone number

        :param: header: the dict is provided from request
                user_data: the user data is provided from request

        :return: return a user record object or exception
        :Raises: CustomException: a custom exception
    """
    _validate_input_form( header, form_data)
    """
    create a newly user record,
    if we have any database internal id
    should return with bad request 400
    """
    if form_data.get('user_id'):
        raise CustomException('The user id already existed', '400', {'field': 'user_id',
                                                                     'code': 'USR_0'})
    """
    Transform request object to backend object, and fixup all mismatching fields.
    even though all of them might be the same, but We want to make sure they are all the same.
    """
    db_object = defaultdict()
    """
    required field should always expected
    """
    if not form_data['account']:
        raise CustomException('The user phone is missing', '400', {'field': 'phone',
                                                                   'code': 'USR_0'})

    if not form_data['email']:
        raise CustomException('The email is missing', '400', {'field': 'email',
                                                              'code': 'USR_0'})
    db_object['email'] = form_data['email']
    if Dal.get_user_by(**db_object):
        raise CustomException('The email already in use', '400', {'field': 'email',
                                                                  'code': 'USR_03'})

    db_object['account'] = form_data['account']

    if Dal.get_user_by(**db_object):
        raise CustomException('The phone already in use', '400', {'field': 'phone',
                                                                  'code': 'USR_03'})

    """
    fields is created/set by system.
    user_uuid
    active
    external_user
    """
    db_object['user_uuid'] = _createUUID4()
    db_object['active'] = True
    db_object['external_user'] = True

    """
    optional fields.
    """
    db_object['first_name'] = form_data['first_name']
    db_object['last_name'] = form_data['last_name']
    db_object['country'] = form_data['country']
    db_object['province'] = form_data['province']
    db_object['city'] = form_data['city']
    db_object['address_line'] = form_data['address_line']
    db_object['postal_code'] = form_data['postal_code']
    db_object['firebase_uid'] = form_data['firebase_uid']
    return Dal.create_user(**db_object)


def get_user_profile(**data):
    """

    :param data: The dict to query the data.
    :return: the user record data or a custom exception.
    """
    if not data or data == '':
        raise CustomException('The query is empty', '400', {'field': 'user_id',
                                                            'code': 'USR_0'})
    _user_obj = Dal.get_user_by(**data)
    if not _user_obj:
        raise CustomException('The user have not added into database', '500', {'field': 'unknown',
                                                                               'code': 'USR_0'})
    return _user_obj


def get_all_users():
    """
    Retrieve all users.
    :return:
    """
    return Dal.get_all()


def delete_users():
    """
    Delete all users
    :return: True if success or an exception
    """
    objs = Dal.get_all()
    for obj in objs:
        obj.delete()
    return True


def delete_user(user_uuid):
    """
    Delete a specific user
    :param user_uuid: a internal user uuid4
    Ex: 00489c22-94bd-4490-8ecb-da29fba3d854
    :return: True if success or a exception
    """
    user = Dal.get_user_by(user_uuid=user_uuid)
    if not user:
        raise CustomException('The user have not added into database', '500', {'field': 'user_uuid',
                                                                               'code': 'USR_0'})
    user.delete()
    return True