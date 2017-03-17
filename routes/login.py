from handler.blog_handler import BlogHandler
from utils.hash_utils import HashUtils
from entities.user import User

class Login(BlogHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        user = self.request.get('user')
        password = self.request.get('password')

        user_db = User.get_user(user)

        hash = HashUtils.crypt(password, user_db.salt)

        user_has_permission = HashUtils.hasPermission(password, user_db.salt, hash)
        if user_has_permission:
            self.response.set_cookie('user_id', user_db.hash)
            self.response.set_cookie('user_desc', user_db.user)
            self.redirect('/main?user=' + user_db.user)
        else:
            self.render('login.html', error_message = 'User or password are wrong')