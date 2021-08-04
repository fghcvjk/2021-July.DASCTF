from hypercorn.middleware import DispatcherMiddleware
from vuln_app import vuln_app
from simple_app import simple_app
dispatcher_app = DispatcherMiddleware({
    "/vuln": vuln_app,
    "/": simple_app,
})

if __name__ == '__main__':
    a = 1
