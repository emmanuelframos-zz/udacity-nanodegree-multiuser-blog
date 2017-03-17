from validator.signin_validator import SignInValidator
from handler.blog_handler import BlogHandler
from utils.hash_utils import HashUtils
from entities.user import User

import datetime

class SignIn(BlogHandler):

    def get(self):
        self.render('signin.html')

    def post(self):
        user = self.request.get('user')
        fullname = self.request.get('fullname')
        password = self.request.get('password')

        params = dict()
        have_error = SignInValidator.user_data_are_valid(fullname, user, password, params)

        if have_error:
            self.render('signin.html', **params)
        else:
            salt = HashUtils.gen_salt();
            hash = HashUtils.crypt(password, salt)

            u = User(user=user, fullname=fullname, hash=hash, salt=salt, created=datetime.datetime.now())
            u.put()

            self.redirect('/main?user=' + user)