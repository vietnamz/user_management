from api import db
import datetime


class User(db.Model):
    """This class represents the various makes and models of user table
    It corresponds to the user table"""

    __tablename__ = 'um_user'

    """
    required fields:
    """
    user_id = db.Column(name='user_id',
                        type_=db.Integer,
                        primary_key=True,
                        nullable=False,
                        autoincrement=True,
                        comment='Unique Identifier for each User.')

    user_uuid = db.Column(name='user_uuid',
                          type_=db.String,
                          index=True,
                          unique=True,
                          comment="Internal user uuid")

    """
    The system format should be consistent
    phone number MUST be as below format, that frontend should transform accordingly.
    Ex:
    +84939717135
    """
    account = db.Column(name='account',
                        type_=db.String(255),
                        nullable=True,
                        comment='Name of this users login account.',
                        index=True)

    email = db.Column(name='email',
                      type_=db.String(255),
                      nullable=False,
                      index=True,
                      unique=True,
                      comment='email of user')
    """
    Optional fields.
    """
    gender = db.Column(name='gender',
                       type_=db.String(255),
                       default=0,
                       nullable=True,
                       comment='Unknown, Male, Female, or lawful person.')

    first_name = db.Column(name='first_name',
                           type_=db.String(255),
                           nullable=True,
                           comment='Individual Given Name')
    last_name = db.Column(name='last_name',
                          type_=db.String(255),
                          nullable=True,
                          comment='Middle Name or initial.')
    user_note = db.Column(name='user_note',
                          type_=db.String(255),
                          nullable=True,
                          comment='Note about this user.')

    credit_card = db.Column(name='credit_card',
                            type_=db.String(128),
                            nullable=True,
                            comment='The user credit card')
    address_line = db.Column(name='address_line',
                             type_=db.String(255),
                             nullable=True,
                             comment='Address Line')

    city = db.Column(name='city',
                     type_=db.String(128),
                     nullable=True,
                     comment='City')
    province = db.Column(name='province',
                         type_=db.String(128),
                         nullable=True,
                         comment='province')
    postal_code = db.Column(name='postal_code',
                            type_=db.String(64),
                            nullable=True,
                            comment='postal code for asia country')
    country = db.Column(name='country',
                        type_=db.String(255),
                        nullable=True,
                        comment='country')
    mob_phone = db.Column(name='mob_phone',
                          type_=db.String(64),
                          nullable=True,
                          comment='Mobile phone')

    thumbnail = db.Column(name='thumbnail',
                          type_=db.String(255),
                          nullable=True,
                          comment='Thumbnail photo')

    avatar = db.Column(name='avatar',
                       type_=db.String(255),
                       nullable=True,
                       comment='avatar photo')

    external_user = db.Column(name='external_user',
                              type_=db.Boolean,
                              default=False,
                              nullable=True,
                              comment='If true, this user gets external email instead of internal messages.')

    active = db.Column(name='active',
                       type_=db.Boolean,
                       default=True,
                       nullable=True,
                       comment='If true, this entry is still active.')

    create_date = db.Column(name='created_date',
                            type_=db.DateTime,
                            nullable=True,
                            default=datetime.datetime.utcnow,
                            comment='Created date')

    updated_date = db.Column(name='modified_date',
                             type_=db.DateTime,
                             comment='update date')

    firebase_uid = db.Column(name='firebase_uid',
                              type_=db.String(255),
                              comment='Firebase User Id')

    def __init__(self, **kwargs):
        self.update(**kwargs)

    def update(self, **kwargs):
        if kwargs.get('user_id'):
            self.user_id = kwargs.pop( 'user_id' )
        if kwargs.get('user_uuid'):
            self.user_uuid = kwargs.pop('user_uuid')
        if kwargs.get('email'):
            self.email = kwargs.pop('email')
        if kwargs.get('account'):
            self.account = kwargs.pop('account')

        if kwargs.get('first_name'):
            self.first_name = kwargs.pop('first_name')
        if kwargs.get('last_name'):
            self.last_name = kwargs.pop('last_name')
        if kwargs.get('gender'):
            self.gender = kwargs.pop('gender')
        if kwargs.get('user_note'):
            self.user_note = kwargs.pop('user_note')
        if kwargs.get('credit_card'):
            self.credit_card = kwargs.pop('credit_card')
        if kwargs.get('address_line'):
            self.address_line = kwargs.pop('address_line')
        if kwargs.get('city'):
            self.city = kwargs.pop('city')
        if kwargs.get('address_line'):
            self.address_line = kwargs.pop('address_line')
        if kwargs.get('province'):
            self.province = kwargs.pop('province')
        if kwargs.get('postal_code'):
            self.postal_code = kwargs.pop('postal_code')
        if kwargs.get('country'):
            self.country = kwargs.pop('country')
        if kwargs.get('mob_phone'):
            self.mob_phone = kwargs.pop('mob_phone')
        if kwargs.get('thumbnail'):
            self.thumbnail = kwargs.pop('thumbnail')
        if kwargs.get('avatar'):
            self.avatar = kwargs.pop('avatar')
        if kwargs.get('create_date'):
            self.create_date = kwargs.pop('create_date')
        if kwargs.get('updated_date'):
            self.updated_date = kwargs.pop('updated_date')
        if kwargs.get('firebase_uid'):
            self.firebase_uid = kwargs.pop('firebase_uid')
        if kwargs.get('external_user'):
            self.external_user = kwargs.pop('external_user')
        if kwargs.get('active'):
            self.active = kwargs.pop('active')

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.user_id

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_user_by(**kwargs):
        user = User.query.filter_by(**kwargs).first()
        return user

    @staticmethod
    def get_all():
        return User.query.all()

    def __repr__(self):
        return "<{}: {} {} {}>".format(self.__class__.__name__, self.user_id, self.email, self.user_uuid)
