import webapp2
import jinja2

class BlogHandler(webapp2.RequestHandler):

    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, html_template, **kw):
        template = jinja_env.get_template(html_template)
        result = template.render(**kw)
        self.write(result)