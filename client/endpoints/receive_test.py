from endpoints import endpoint


@endpoint('receive-test')
def receive_test(client, data):
    print('received test')
    print(data['message'])
