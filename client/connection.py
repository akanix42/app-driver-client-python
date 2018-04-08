from autobahn.twisted.websocket import WebSocketClientProtocol, \
    WebSocketClientFactory
from twisted.internet.protocol import ReconnectingClientFactory

from twisted.python import log
from twisted.internet import reactor

import sys
import json
import settings


class OuterSscope:
    client = None


def send_message(message):
    if not OuterSscope.client:
        return
    OuterSscope.client.sendMessage(message, False)


class AppDriverClientProtocol(WebSocketClientProtocol):

    def onOpen(self):
        OuterSscope.client = self

    def onMessage(self, payload, isBinary):
        try:
            if not isBinary:
                data = json.loads(payload.decode('utf8'))
                from endpoints import endpoints
                endpoints[data[u'endpoint']](data)

                print("Result received: {}".format(data))
        except Exception as ex:
            self.sendMessage(str(ex))

    def onClose(self, wasClean, code, reason):
        if reason:
            print(reason)
        reactor.stop()
        OuterSscope.client = None


class AppDriverClientFactory(WebSocketClientFactory, ReconnectingClientFactory):
    protocol = AppDriverClientProtocol

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed - retrying')
        self.retry(connector)

    def clientConnectionLost(self, connector, reason):
        print('Connection lost - retrying')
        self.retry(connector)


log.startLogging(sys.stdout)

factory = AppDriverClientFactory(u'ws://{settings.address}:{settings.port}'.format(settings = settings))
factory.maxDelay = 15

reactor.connectTCP(settings.address, settings.port, factory)
reactor.run()
