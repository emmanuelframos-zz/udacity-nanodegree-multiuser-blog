import datetime
import time

from google.appengine.ext import ndb
from handler.blog_handler import BlogHandler
from entities.post import Post
from entities.user import User

class GetPost(BlogHandler):
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

        self.render('post.html', post = post_from_db)

class NewPost(BlogHandler):
    """
    Class that handles a new post entry route
    """

    def get(self):
        """
        Renders a new post page if user is authenticated, if no redirects to login route
        :return: 
        """
        if User.is_authenticated(self.request.cookies.get('user_id')):
            self.render('post.html', post=Post(title="", content = ""))
        else:
            self.redirect('/login')

    @BlogHandler.is_authenticated
    def post(self):
        """
        Creates or update a new post entry if user is authenticated, if no redirects to login route
        :return: 
        """
        user_desc = self.request.cookies.get('user_desc')

        title = self.request.get('title')
        content = self.request.get('content')

        if 'update' in self.request.POST:
            post_id = self.request.get('id')
            post = Post.get_by_id(post_id)

            post.title = title
            post.content = content
            post.last_modified = datetime.datetime.now()

            post.put()

            time.sleep(2)
        elif 'create' in self.request.POST:
            title = self.request.get('title')
            content = self.request.get('content')

            user = User.get_user(user_desc)

            p = Post(author=user.user, title=title, content = content, created = datetime.datetime.now(), last_modified = datetime.datetime.now())
            p.put()

            time.sleep(2)

        self.redirect('/main')

class RemovePost(BlogHandler):
    """
    Class that handles a post removing route
    """
    @BlogHandler.is_authenticated
    def post(self):
        """
        Removes a post entry if user is authenticated, if no redirects to login route
        :return: 
        """
        post_id = self.request.get('id')
        user_desc = self.request.cookies.get('user_desc')

        post = Post.get_by_id(post_id)

        if Post.is_post_owner(user_desc, post):
            post.key.delete()
            time.sleep(2)

        self.redirect('/main')