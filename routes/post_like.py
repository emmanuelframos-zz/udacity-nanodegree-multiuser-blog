import time

from google.appengine.ext import ndb
from handler.blog_handler import BlogHandler
from entities.post import Post
from entities.user import User

class PostLike(BlogHandler):
    """
    Class that handles a post like and unlike route
    """

    def post(self):
        """
        Creates a post like or unlike if user is authenticated, if no redirects to login route
        :return: 
        """
        if User.is_authenticated(self.request.cookies.get('user_id')):
            user_desc = self.request.cookies.get('user_desc')
            post_id = self.request.get('id_post')
            post = Post.get_by_id(post_id)

            if not Post.is_post_owner(user_desc, post):
                if 'like' in self.request.POST:
                    post.likes.append(user_desc)
                elif 'unlike' in self.request.POST:
                    post.likes.remove(user_desc)

                post.put()

                time.sleep(2)

            self.redirect('/main')
        else:
            self.redirect('/login')