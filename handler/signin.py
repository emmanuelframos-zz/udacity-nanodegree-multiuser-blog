import time

from validator.signin_validator import SignInValidator
from handler.base import BlogHandler
from utils.hash_utils import HashUtils
from entities.user import User

import datetime


class SignInHandler(BlogHandler):
    """
    Class that handles a sign in route
    """

    def get(self):
        """
        Renders the sign in page
        :return: 
        """
        self.render('signin.html')

    def post(self):
        """
        Creates a user entry if user date is valid, 
        if no sends an error message
        :return: 
        """
        user = self.request.get('user')
        fullname = self.request.get('fullname')
        password = self.request.get('password')

        params = dict()
        have_error = SignInValidator\
            .user_data_are_valid(fullname, user, password, params)

        if have_error:
            self.render('signin.html', **params)
        else:
            salt = HashUtils.gen_salt()
            hash = HashUtils.crypt(password, salt)

            u = User(user=user, fullname=fullname,
                     hash=hash, salt=salt,
                     created=datetime.datetime.now())
            u.put()

            time.sleep(2)

            self.response.set_cookie('user_id', u.hash)
            self.response.set_cookie('user_desc', u.user)

            self.redirect('/main')