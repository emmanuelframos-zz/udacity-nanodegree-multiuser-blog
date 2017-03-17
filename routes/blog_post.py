import datetime
import time

from handler.blog_handler import BlogHandler
from entities.post import Post
from entities.user import User

class GetPost(BlogHandler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id))
        post = db.get(key)

        if not post:
            self.error(404)
            return
    #Show post not found page

class NewPost(BlogHandler):

    def get(self):
        post_id = self.request.get('id')
        post = Post.get_by_id(post_id)
        self.render('post.html', post=post)

    def post(self):
        if 'save-post' in self.request.POST:
            subject = self.request.get('subject')
            content = self.request.get('content')

            user = User.get_user_by_hash(self.request.cookies.get('user_id'))

            p = Post(author=user, subject=subject, content = content, created = datetime.datetime.now(), last_modified = datetime.datetime.now())
            p.put()

            time.sleep(5)

        self.redirect('/main?user=' + self.request.cookies.get('user_desc'))