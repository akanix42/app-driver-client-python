import json

from ws4py.client.threadedclient import WebSocketClient
from endpoints import endpoints
import settings


class AppDriverClient(WebSocketClient):
    # def opened(self):
    #     def data_provider():
    #         for i in range(1, 200, 25):
    #             yield "#" * i
    #
    #     self.send(data_provider())
    #
    #     for i in range(0, 200, 25):
    #         print(i)
    #         self.send("*" * i)

    def closed(self, code, reason):
        print("Closed down", code, reason)

    def received_message(self, message):
        #try:
            print('received message ')
            print("=> %d %s" % (len(message), str(message)))
            data = json.loads(str(message))
            # print(data['response'])
            endpoint = data.get('endpoint')
            if endpoint:
                endpoints[endpoint](self, data)
        #except Exception as e:
         #   print('An error occurred: ', str(e))
        # if message == 'test':
        #     print('test message received')
        # print(message)
        # if len(m) == 175:
        #     self.close(reason = 'Bye bye')

    def send_message(self, message):
        self.send(json.dumps(message))

# if __name__ == '__main__':
connection = AppDriverClient(u'ws://{settings.address}:{settings.port}'.format(settings = settings),
                         protocols = ['http-only', 'chat'])
connection.daemon = False
try:
    connection.connect()
except Exception as e:
    print(str(e))

