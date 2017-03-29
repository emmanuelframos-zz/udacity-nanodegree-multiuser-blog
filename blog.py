import webapp2

from routes.home import Home
from routes.signin import SignIn
from routes.login import Login
from routes.main import Main
from routes.post import NewPost
from routes.post import GetPost
from routes.post import RemovePost
from routes.post_comment import PostComment
from routes.post_comment import EditPostComment
from routes.logout import Logout
from routes.post_like import PostLike

'''
Routes Configuration
Home: the root of application
Login: the login page
Logout: clear all cookies and detach user
SignIn: the sign in page
Main: main page where posts are listed
NewPost: page to create or update a post
GetPost: page that returns a specific post with filled data
RemovePost: removes a post 
PostComment: creates a post comment
EditPostComment: update or remove a post comment
PostLike: create or remove a post like
'''

app = webapp2.WSGIApplication([
   ('/', Home),
   ('/login', Login),
   ('/logout', Logout),
   ('/signIn', SignIn),
   ('/main', Main),
   ('/blogPost/create', NewPost),
   ('/blogPost/get/?', GetPost),
   ('/blogPost/remove', RemovePost),
   ('/blogPost/comment', PostComment),
   ('/blogPost/comment/edit', EditPostComment),
   ('/blogPost/like', PostLike),
   ('/blogPost/unlike', PostLike)
   ],
  debug=True)