import os
import webapp2
import jinja2
from entities.user import User


class BlogHandler(webapp2.RequestHandler):
    """
    Handler class that writes templates on response
    """
    template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir),
        autoescape=True)

    def render(self, html_template, **params):
        """
        Renders the template using params
        :param html_template: Template file name
        :param params: Params to write
        :return: 
        """
        template = BlogHandler.jinja_env\
            .get_template(html_template)\
            .render(**params)

        self.response.out.write(template)

    @staticmethod
    def is_authenticated(func):
        """
        A decorator to confirm if an user is logged in or redirect as needed
        """

        def login(self, *args, **kwargs):
            user_id = self.request.cookies.get('user_id')
            if user_id and len(user_id) > 0 and User.is_authenticated(user_id):
                func(self, *args, **kwargs)
            else:
                self.redirect("/login")

        return login