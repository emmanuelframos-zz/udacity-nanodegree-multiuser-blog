from google.appengine.ext import ndb
from handler.base import BlogHandler
from entities.post import Post


class GetPostHandler(BlogHandler):
    """
    Class that handles getting post route
    """
    @BlogHandler.is_authenticated
    def get(self):
        """
        Get the post if user is authenticated, if no redirects to login route
        :return: 
        """
        post_id = self.request.get('id')
        post_from_db = ndb.Key(Post, int(post_id)).get()

        if not post_from_db:
            self.redirect('/main')

        self.render('post.html', post=post_from_db)