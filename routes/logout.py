from handler.blog_handler import BlogHandler

class Logout(BlogHandler):

    def get(self):
        self.response.delete_cookie('user_id')
        self.response.delete_cookie('user_desc')
        self.redirect('/login')