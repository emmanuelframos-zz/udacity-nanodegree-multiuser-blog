import datetime
import time

from google.appengine.ext import ndb
from handler.base import BlogHandler
from entities.post import Post
from entities.user import User


class NewPostHandler(BlogHandler):
    """
    Class that handles a new post entry route
    """

    def get(self):
        """
        Renders a new post page if user is authenticated, 
        if no redirects to login route
        :return: 
        """
        if User.is_authenticated(self.request.cookies.get('user_id')):
            self.render('post.html', post=Post(title="", content= ""))
        else:
            self.redirect('/login')

    @BlogHandler.is_authenticated
    def post(self):
        """
        Creates or update a new post entry if user is 
        authenticated, if no redirects to login route
        :return: 
        """
        user_id = self.request.cookies.get('user_id')
        post_id = self.request.get('id')
        title = self.request.get('title')
        content = self.request.get('content')

        if 'update' in self.request.POST:
            post = Post.get_by_id(post_id)

            if Post.is_post_owner(user_id, post):
                post.title = title
                post.content = content
                post.last_modified = datetime.datetime.now()

                post.put()

                time.sleep(2)
        elif 'create' in self.request.POST:
            title = self.request.get('title')
            content = self.request.get('content')

            user = User.get_by_hash(user_id)

            p = Post(author=user.user, title=title,
                     content=content, created=datetime.datetime.now(),
                     last_modified=datetime.datetime.now())
            p.put()

            time.sleep(2)

        self.redirect('/main')