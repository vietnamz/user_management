"""
integration test.
"""

import requests
import atexit

from pact import Consumer, Provider
from pytest import mark


USER_MANAGEMENT = 'http://localhost:5001'


def get_users():
    """Fetch all users"""
    print("{}/users/api/v1/user/{}".format(USER_MANAGEMENT))
    return requests.get(
        "{}/users/api/v1/user/{}".format(USER_MANAGEMENT),
        params=None,
        headers={'Content-Type': 'application/json'}
    ).json()


def get_user(user_uuid):
    """Fetch a specific user"""
    print("{}/users/api/v1/{}".format(USER_MANAGEMENT, user_uuid))
    return requests.get(
        "{}/users/api/v1/user".format(USER_MANAGEMENT),
        params=None,
        headers={'Content-Type': 'application/json'}
    ).json()


def test_user_creation():

    expected = {
            "user_id": 1,
            "gender": "0",
            "account": "+84939717135",
            "email": "delgemoon@gmail.com",
            "first_name": None,
            "last_name": None,
            "user_note": None,
            "credit_card": None,
            "address_line": "Cong Hoa",
            "city": "Hcm",
            "province": None,
            "postal_code": "8976451",
            "country": "Vietnam",
            "thumbnail": None,
            "avatar": None,
            "mob_phone": None,
            "external_user": True,
            "active": True,
            "create_date": "2020-07-07T05:26:06.703290",
            "updated_date": None,
            "firebase_uid": "68BQeiGHEUgklhQsuSZagrdfeU72",
            "user_uuid": "3aa6d164-e287-4ce8-a759-694a1ba93dbc"
        }

    result = get_user('3aa6d164-e287-4ce8-a759-694a1ba93dbc')
    assert result == expected