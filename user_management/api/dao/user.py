from flask_restplus import fields
from api import api
from flask_restplus import reqparse

"""
User data object response.
"""
user = api.model('schema', {
    'user_id': fields.Integer(description='The user identifier', example='The unique identifier of user'),
    'gender': fields.String(description='user gender', example="Female"),
    'account': fields.String(description='the account name', example='+84 939717135'),
    'email': fields.String(description='User Email', example='delgemoon@gmail.com'),
    'first_name': fields.String(description='The user common name', example='Nhi'),
    'last_name': fields.String(description='The user given name', example='Dang'),
    'user_note': fields.String(description='The user note', example='This is a admin user'),
    'credit_card': fields.String(description='The user credit card', example='xxxxxxxxxxx'),
    'address_1': fields.String(description='The first address of user', example='Sai gon'),
    'address_2': fields.String(description='The second address of user', example='Truong Chinh'),
    'city': fields.String(description='the user city', example='Sai Gon'),
    'province': fields.String(description='The province of user coutry', example='Asia'),
    'postal_code': fields.String(description='The postal code', example=''),
    'country': fields.String(description='The user country', example='Viet Nam'),
    'thumbnail': fields.String(description='thumbnail photo', example='http://photo.com/photo.jpg'),
    'avatar': fields.String(description='avatar photo', example='http://photo.com/photo.jpg'),
    'mob_phone': fields.String(description='mobile phone', example="+351323213511235"),
    'external_user': fields.Boolean(description='True if the user from external source like phone number',
                                    example=True),
    'active': fields.Boolean(description='True if the user is active', example=True),
    'create_date': fields.DateTime(description='when this user was created', example=''),
    'updated_date': fields.DateTime(description='', example=''),
    'firebase_uid': fields.String(description='Firebase identifier',
                                  example='WAbnB0SU2DWeu5mgaKaXmxw3Zb62'),
    'user_uuid': fields.String(description='Internal user identifier',
                               example='3525fbc5-9485-4645-b482-5c72d01a1543')
})

"""
response transformation
"""

"""
request transformation and validation.
"""

query_params1 = reqparse.RequestParser()
query_params1.add_argument('user_id', required=False, type=int, location='args', help='internal database id')
query_params1.add_argument('phone', required=False, type=str , location='args', help='user phone')
query_params1.add_argument('email', required=False, type=str, location='args', help='user email')

newly_user_data = reqparse.RequestParser()
newly_user_data.add_argument('account', required=True, type=str, location='form', help='unique phone of user')
newly_user_data.add_argument('email', required=True, type=str, location='form', help="email of User.")
newly_user_data.add_argument('firebase_uid', required=False, type=str, location='form', help='firebase user id')
newly_user_data.add_argument('first_name', required=False, type=str, location='form', help="First name.")
newly_user_data.add_argument('last_name', required=False, type=str, location='form', help="Last name.")
newly_user_data.add_argument('country', required=False, type=str, location='form', help="user country.")
newly_user_data.add_argument('province', required=False, type=str, location='form', help="user province.")
newly_user_data.add_argument('city', required=False, type=str, location='form', help="user city.")
newly_user_data.add_argument('address_line', required=False, type=str, location='form', help="user address line.")
newly_user_data.add_argument('postal_code', required=False, type=str, location='form', help="user postal code.")
newly_user_data.add_argument('mob_phone', required=False, type=str, location='form', help='phone of user')

user_data = reqparse.RequestParser()
user_data.add_argument('body', required=False, type=list, location='json', help='user updated data body')

