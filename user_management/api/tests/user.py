import requests
import atexit

from pact import Consumer, Provider
from pytest import mark


USER_MANAGEMENT = 'http://192.168.100.3:5001'


def get_user(user_uuid):
    """Fetch the panel efficiency of a known inefficient panel"""
    print("{}/users/{}".format(USER_MANAGEMENT, user_uuid))
    return requests.get(
        "{}/users/{}".format(USER_MANAGEMENT, user_uuid),
        params=None,
        headers={'Content-Type': 'application/json'}
    ).json()


pact = Consumer('User Management Service').has_pact_with(Provider('Service'), host_name="192.168.100.3", port=5000)
pact.start_service()
atexit.register(pact.stop_service)


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


    pact.given(
        'a url'
    ).upon_receiving(
        'a request for predefined user with user uuid 3aa6d164-e287-4ce8-a759-694a1ba93dbc'
    ).with_request(
         'get',
         '/users/users/3aa6d164-e287-4ce8-a759-694a1ba93dbc'
     ).will_respond_with(200)

    pact.setup()
    result = get_user('3aa6d164-e287-4ce8-a759-694a1ba93dbc')
    pact.verify()
    assert result == expected