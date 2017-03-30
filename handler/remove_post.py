import time

from google.appengine.ext import ndb
from handler.base import BlogHandler
from entities.post import Post


class RemovePostHandler(BlogHandler):
    """
    Class that handles a post removing route
    """
    @BlogHandler.is_authenticated
    def post(self):
        """
        Removes a post entry if user is authenticated, 
        if no redirects to login route
        :return: 
        """
        post_id = self.request.get('id')

        post = Post.get_by_id(post_id)

        if Post.is_post_owner(self.request.cookies.get('user_id'), post):
            post.key.delete()
            time.sleep(2)

        self.redirect('/main')