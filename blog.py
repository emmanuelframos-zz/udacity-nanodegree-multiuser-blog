import webapp2

from routes.home import Home
from routes.signin import SignIn
from routes.login import Login
from routes.main import Main
from routes.blog_post import NewPost
from routes.blog_post import GetPost
from routes.logout import Logout

'''
Routes Configuration - We have six routes in application
Home: the root of application
Login: the login page
SignIn: the sign in page
Main: main page where posts are listed
NewPost: page to create a post
GetPost: page that returns a specific post with filled data
Logout: clear all cookies and detach user
'''
app = webapp2.WSGIApplication([
                                   ('/', Home),
                                   ('/login', Login),
                                   ('/signIn', SignIn),
                                   ('/main/?', Main),
                                   ('/post', NewPost),
                                   ('/post?id=([0-9]+)', GetPost),
                                   ('/logout', Logout)
                                   ],
                                  debug=True)