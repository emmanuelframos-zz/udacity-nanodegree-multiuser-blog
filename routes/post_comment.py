import datetime
import time

from google.appengine.ext import ndb
from handler.blog_handler import BlogHandler
from entities.post import Post
from entities.user import User
from entities.comment import Comment

class PostComment(BlogHandler):
    """
    Class that handles a post comment route
    """

    def post(self):
        """
        Creates a new comment in a post if user is authenticated, if no redirects to login route
        :return: 
        """
        if User.is_authenticated(self.request.cookies.get('user_id')):
            post_id = self.request.get('id')
            user_desc = self.request.cookies.get('user_desc')
            comment = self.request.get('comment')

            post = Post.get_by_id(post_id)
            user = User.get_user(user_desc)

            comment = Comment(author=user.user, post=post.key.id(), comment=comment, created=datetime.datetime.now(), last_modified=datetime.datetime.now())
            comment.put()

            time.sleep(2)

            self.redirect('/main')
        else:
            self.redirect('/login')

class EditPostComment(BlogHandler):
    """
    Class that handles a post comment route
    """

    def post(self):
        """
        Updates or removes a new comment in a post if user is authenticated, if no redirects to login route
        :return: 
        """
        if User.is_authenticated(self.request.cookies.get('user_id')):
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
        else:
            self.redirect('/login')