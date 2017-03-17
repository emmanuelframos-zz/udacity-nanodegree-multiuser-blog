from handler.blog_handler import BlogHandler
from entities.post import Post

class Main(BlogHandler):

    def get(self):
        posts = Post.get_posts()
        self.render('main.html', posts = posts)