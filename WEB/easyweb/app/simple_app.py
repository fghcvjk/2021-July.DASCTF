from a2wsgi import WSGIMiddleware
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
simple_app = WSGIMiddleware(application)