from handler.blog_handler import BlogHandler
from entities.user import User

class Home(BlogHandler):
  """
  Class that handles home route  
  """

  def get(self):
      """
      Checks if user is authenticated, if yes redirects to main route, if no redirects to login route
      :return: 
      """
      if 'user_id' in self.request.cookies:
         if User.is_authenticated(self.request.cookies.get('user_id')):
            self.redirect('/main')
         else:
            self.response.delete_cookie('user_id')
            self.response.delete_cookie('user_desc')

            self.redirect('/login')
      else:
         self.redirect('/login')