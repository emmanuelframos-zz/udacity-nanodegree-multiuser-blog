import datetime
import time

from google.appengine.ext import ndb
from handler.base import BlogHandler
from entities.post import Post
from entities.user import User
from entities.comment import Comment


class NewPostCommentHandler(BlogHandler):
    """
    Class that handles a post comment route
    """

    @BlogHandler.is_authenticated
    def post(self):
        """
        Creates a new comment in a post if user is authenticated,
        if no redirects to login route
        :return: 
        """
        post_id = self.request.get('id')
        user_id = self.request.cookies.get('user_id')
        comment = self.request.get('comment')

        post = Post.get_by_id(post_id)
        user = User.get_by_hash(user_id)

        comment = Comment(author=user.user, post=post.key.id(),
                          comment=comment, created=datetime.datetime.now(),
                          last_modified=datetime.datetime.now())
        comment.put()

        time.sleep(2)

        self.redirect('/main')