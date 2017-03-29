from handler.blog_handler import BlogHandler
from utils.hash_utils import HashUtils
from entities.user import User

class Login(BlogHandler):
    """
    Class that handles login route
    """

    def get(self):
        """
        Renders the login template
        :return: 
        """
        self.render('login.html')

    def post(self):
        """
        Checks if user login in valid, if yes redirect to main route, if no sends an error message
        :return: 
        """
        user = self.request.get('user')
        password = self.request.get('password')
        error_message = ""

        user_from_db = User.get_user(user)

        if not user_from_db:
            error_message = 'User does not exists, please sign in'
        else:
            user_has_permission = HashUtils.hasPermission(password, user_from_db.salt, user_from_db.hash)

            if user_has_permission:
                self.response.set_cookie('user_id', user_from_db.hash)
                self.response.set_cookie('user_desc', user_from_db.user)
                self.redirect('/main')
            else:
                error_message = 'User or password are wrong'

        self.render('login.html', error_message = error_message)