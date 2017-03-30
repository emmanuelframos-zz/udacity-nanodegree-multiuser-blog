from handler.base import BlogHandler


class LogoutHandler(BlogHandler):
    """
    Class that handles logout route
    """

    def get(self):
        """
        Detach user, cleaning cookies and redirecting to login route
        :return: 
        """
        self.response.delete_cookie('user_id')
        self.response.delete_cookie('user_desc')
        self.redirect('/login')