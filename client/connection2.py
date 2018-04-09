import websocket

import settings


def on_message(ws, message):
    print 'message!'
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print 'socket open'


websocket.enableTrace(True)
connection = websocket.WebSocketApp(
    u'ws://{settings.address}:{settings.port}'.format(settings = settings),
    on_message = on_message,
    on_error = on_error,
    on_close = on_close,
    on_open = on_open)

# connection.run_forever()
