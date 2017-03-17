import os
import webapp2
import jinja2

class BlogHandler(webapp2.RequestHandler):

    template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
    jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

    def render(self, html_template, **params):
        template = BlogHandler.jinja_env.get_template(html_template).render(**params)
        self.response.out.write(template)