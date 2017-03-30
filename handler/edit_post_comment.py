import datetime
import time

from google.appengine.ext import ndb
from handler.base import BlogHandler
from entities.comment import Comment


class EditPostCommentHandler(BlogHandler):
    """
    Class that handles a post comment route
    """

    @BlogHandler.is_authenticated
    def post(self):
        """
        Updates or removes a new comment in a post if user is 
        authenticated, if no redirects to login route
        :return: 
        """
        comment_id = self.request.get('id_comment')

        comment = Comment.get_by_id(comment_id)

        if comment.author == self.request.cookies.get('user_desc'):
            if 'update-comment' in self.request.POST:
                comment.comment = self.request.get('comment_desc')
                comment.last_modified = datetime.datetime.now()
                comment.put()
            elif 'remove-comment' in self.request.POST:
                comment.key.delete()

            time.sleep(2)

        self.redirect('/main')