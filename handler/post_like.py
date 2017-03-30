import time

from google.appengine.ext import ndb
from handler.base import BlogHandler
from entities.post import Post
from entities.user import User


class PostLikeHandler(BlogHandler):
    """
    Class that handles a post like and unlike route
    """

    @BlogHandler.is_authenticated
    def post(self):
        """
        Creates a post like or unlike if user is authenticated, 
        if no redirects to login route
        :return: 
        """
        user_id = self.request.cookies.get('user_id')
        post_id = self.request.get('id_post')

        user = User.get_by_hash(user_id)
        post = Post.get_by_id(post_id)

        if self.like_parameters_are_valid(user, post_id, post):
            if self.can_like(user, post):
                post.likes.append(user.user)
                post.put()
            elif self.can_unlike(user, post):
                post.likes.remove(user.user)
                post.put()

            time.sleep(2)

        self.redirect('/main')

    def like_parameters_are_valid(self, user, post_id, post):
        return user and post_id and post

    def can_like(self, user, post):
        return not Post.is_post_owner(user.hash, post) \
               and 'like' in self.request.POST \
               and user.user not in post.likes

    def can_unlike(self, user, post):
        return not Post.is_post_owner(user.hash, post) \
               and 'unlike' in self.request.POST \
               and user.user in post.likes