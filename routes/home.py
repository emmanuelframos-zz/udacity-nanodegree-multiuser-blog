from handler.blog_handler import BlogHandler
from entities.user import User

class Home(BlogHandler):

  def get(self):
      if 'user_id' in self.request.cookies:
         user_db = User.get_user_by_hash(self.request.cookies.get('user_id'))
         if user_db:
            self.redirect('/main?user=' + user_db.user)
         else:
            self.response.delete_cookie('user_id')
            self.response.delete_cookie('user_desc')

            self.redirect('/login')
      else:
         self.redirect('/login')