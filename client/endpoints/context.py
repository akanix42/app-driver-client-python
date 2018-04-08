from client.endpoints.endpoints import endpoints


def context_endpoint(data):
    print 'got context'


endpoints.context = context_endpoint
