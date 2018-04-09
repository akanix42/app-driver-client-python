endpoints = {}


def endpoint(name):
    def register_endpoint(fn):
        endpoints[name] = fn
    return register_endpoint
