#!/usr/bin/env python
import os
import jinja2
import webapp2
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates") #povemo da  od tukaj vlekel htmlje
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False) #zazenmo jinjo


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")


class LotoHandler(BaseHandler):
    def get(self):
        random2 = [random.randrange(1, 39) for i in xrange(8)]
        params = {"random1": random2}
        self.render_template("Loto.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),  #poti do handlerjev
    webapp2.Route('/Loto', LotoHandler)
], debug=True)
