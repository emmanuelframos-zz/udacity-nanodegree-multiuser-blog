from handler.blog_handler import BlogHandler
from entities.user import User

class Home(BlogHandler):
  """
  Class that handles home route  
  """

  @BlogHandler.is_authenticated
  def get(self):
      """
      Checks if user is authenticated, if yes redirects to main route, if no redirects to login route
      :return: 
      """
      return