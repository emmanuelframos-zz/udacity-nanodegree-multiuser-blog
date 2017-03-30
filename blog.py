import webapp2

from handler.home import HomeHandler
from handler.login import LoginHandler
from handler.logout import LogoutHandler
from handler.get_post import GetPostHandler
from handler.new_post import NewPostHandler
from handler.remove_post import RemovePostHandler
from handler.edit_post_comment import EditPostCommentHandler
from handler.new_post_comment import NewPostCommentHandler
from handler.post_like import PostLikeHandler
from handler.signin import SignInHandler
from handler.main import MainHandler

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
   ('/', HomeHandler),
   ('/login', LoginHandler),
   ('/logout', LogoutHandler),
   ('/signIn', SignInHandler),
   ('/main', MainHandler),
   ('/blogPost/create', NewPostHandler),
   ('/blogPost/get/?', GetPostHandler),
   ('/blogPost/remove', RemovePostHandler),
   ('/blogPost/comment', NewPostCommentHandler),
   ('/blogPost/comment/edit', EditPostCommentHandler),
   ('/blogPost/like', PostLikeHandler),
   ('/blogPost/unlike', PostLikeHandler)
   ],
  debug=True)