from api.models.user import User

"""
Data access layer. A entry point that we can ingest a cache layer.
"""
class Dal(object):

    """ This static method is used to retrieve user information from a dictionary.
    
        :param: 
        value: the dict is provided
        
        :return:
        return a user row

        :raises Integrity error,

    """
    @staticmethod
    def create_user(**kwargs):
        user = User(**kwargs)
        user.save()
        return user

    @staticmethod
    def get_user_by(**kwargs):
        """ This static method is used to retrieve user information from a dictionary.

            :param:
            value: the dict is provided

            :return:
            return a user row
        """
        return User.get_user_by(**kwargs)


    @staticmethod
    def get_all():
        return User.get_all()