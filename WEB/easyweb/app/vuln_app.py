from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from pyramid.renderers import render_to_response
from pyramid.session import SignedCookieSessionFactory, PickleSerializer
from webob.cookies import Base64Serializer
from a2wsgi import WSGIMiddleware
my_session_factory = SignedCookieSessionFactory("233333333333", serializer=Base64Serializer(PickleSerializer()))


def hello_world(request):
    request.session["233"] = "2333"
    return Response('Hello World!')


vuln_app = None
with Configurator() as config:
    config.set_session_factory(my_session_factory)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    vuln_app  = WSGIMiddleware(config.make_wsgi_app())

if __name__ == '__main__':
    with Configurator() as config:
        config.set_session_factory(my_session_factory)
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()