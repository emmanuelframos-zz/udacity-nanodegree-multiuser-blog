from google.appengine.ext import ndb
from entities.user import User


class Post(ndb.Model):
    """
    Model class that represents a blog post
    """
    author = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    likes = ndb.StringProperty(repeated=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_modified = ndb.DateTimeProperty()

    @staticmethod
    def get_posts():
        """
        Get a post list
        :return: Post[]
        """
        return ndb.gql('select * from Post order by created desc')

    @staticmethod
    def get_by_id(id):
        """
        Get a post by id
        :param id: Post id
        :return: Post
        """
        return ndb.Key('Post', int(id)).get()

    @staticmethod
    def is_post_owner(hash, post):
        """
        Checks if user passed is a post owner
        :param user_id: User login
        :param post: Post object
        :return: True or False
        """
        user = User.get_by_hash(hash)
        return post.author == user.user