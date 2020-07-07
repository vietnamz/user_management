from firebase_admin import auth
from api.exception.invalid_usage import CustomException


def get_user_by_uid(uid):
    """

    :param uid: the firebase user id
    :return: User record object
    """
    user = auth.get_user(uid)
    if not user:
        raise CustomException('The uid is invalid', '401', {'field': 'uid', 'code': 'USR_02'})
    return user


def get_user_by_phone_number( phone ):
    """
    
    :param phone: Phone number to get data
    :return: User record object
    """
    user = auth.get_user_by_phone_number(phone)
    if not user:
        raise CustomException('The phone is invalid', '401', {'field': 'phone', 'code': 'USR_02'})
    print('Successfully fetched user data: {0}'.format(user.uid))
    return user

