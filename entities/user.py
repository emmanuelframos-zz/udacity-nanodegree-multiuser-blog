from google.appengine.ext import db

class User(db.Model):
    user = db.StringProperty(required = True)
    fullname = db.StringProperty(required = True)
    hash = db.StringProperty(required = True)
    salt = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

    @staticmethod
    def get_user(user):
        return db.GqlQuery('select * from User where user = :user_param', user_param=user)[0]

    @staticmethod
    def get_user_by_hash(hash):
        return db.GqlQuery('select * from User where hash = :hash_param', hash_param=hash)[0]