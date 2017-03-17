from google.appengine.ext import db
from entities.user import User

class Post(db.Model):
    author = db.ReferenceProperty(User, collection_name='posts')
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    @staticmethod
    def get_posts():
         return db.GqlQuery('select * from Post order by created desc')

    @staticmethod
    def get_by_id(id):
        return db.GqlQuery('select * from Post where ID = :post_id', post_id=id)