from google.appengine.ext import ndb


class Comment(ndb.Model):
    """
    Model class that represents post comments
    """
    author = ndb.StringProperty(required=True)
    post = ndb.IntegerProperty(required=True)
    comment = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_modified = ndb.DateTimeProperty()

    @staticmethod
    def get_by_id(id):
        """
        Get a comment by id
        :param id: Comment id
        :return: Comment
        """
        return ndb.Key('Comment', int(id)).get()

    @staticmethod
    def get_by_post_id(post_id):
        """
        Get a comment list by post id
        :param post_id: Post id
        :return: Comment[]
        """
        return ndb.gql('select * from Comment where '
                       'post = :post_id_param order by created desc',
                       post_id_param=post_id)