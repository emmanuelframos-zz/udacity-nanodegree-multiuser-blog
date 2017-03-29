from google.appengine.ext import ndb

class User(ndb.Model):
    """
    Model class that represents user
    """
    user = ndb.StringProperty(required = True)
    fullname = ndb.StringProperty(required = True)
    hash = ndb.StringProperty(required = True)
    salt = ndb.StringProperty(required = True)
    created = ndb.DateTimeProperty(auto_now_add = True)

    @staticmethod
    def get_user(user):
        """
        Get user by login
        :param user: User login
        :return: User
        """
        return ndb.gql('select * from User where user = :user_param', user_param=user).get()

    @staticmethod
    def is_authenticated(hash):
        """
        Check if user exists
        :param hash: Hash generated on user sign in hash(password+salt)
        :return: True or False
        """
        return ndb.gql('select * from User where hash = :hash_param', hash_param=hash).get() is not None