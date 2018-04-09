from client.endpoints.endpoints import endpoints


def context_endpoint(data):
    print 'got context'
    print str(data)


endpoints.context = context_endpoint
