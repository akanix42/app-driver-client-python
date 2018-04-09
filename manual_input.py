import click
from client.connection3 import connection


def keypress(x):
    if x == chr(27):
        return False

    if x == "w":
        print "blaw blaw blaw"
    elif x == "a":
        print "blaha blaha blaha"
    elif x == "s":
        print 'send'
        connection.send_message({
            'endpoint': 'client/register',
            'data': 'test',
        })
    elif x == "t":
        print('Client index: ')
        client_index = int(click.getchar())
        connection.send_message({
            'endpoint': 'client/send-test',
            'clientIndex': client_index,
        })
    else:
        print x

    return True


while True:
    try:
        print 'Ready for input:'
        if not keypress(click.getchar()):
            break
    except KeyboardInterrupt:
        connection.close()
        break

# root = Tk()
#
# print "Press a key (Escape key to exit):"
# root.bind_all('<Key>', keypress)
# # don't show the tk window
# root.withdraw()
# root.mainloop()
# # tksupport.install(root)
