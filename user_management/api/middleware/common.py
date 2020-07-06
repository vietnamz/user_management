from api.exception.invalid_usage import CustomException


"""
The common validation logic.
"""


def _validate_input_form(header=None, form_data=None):
    if header and not isinstance(header, dict):
        raise CustomException('The header is not in dict form', '500', {'field': 'header',
                                                                        'code': 'USR_01'})
    if form_data and not isinstance(form_data, dict):
        raise CustomException('The user data is not in dict form', '500', {'field': 'user_data',
                                                                           'code': 'USR_01'})
