from Tkinter import Tk

from twisted.internet import tksupport


def keypress(event):
    from client.connection import OuterSscope, reactor
    if event.keysym == 'Escape':
        from client.connection import reactor
        reactor.stop()
        root.destroy()
    x = event.char
    if x == "w":
        print "blaw blaw blaw"
    elif x == "a":
        print "blaha blaha blaha"
    elif x == "s":
        print "blash blash blash"
    elif x == "d":
        print "blad blad blad"
    else:
        print x


root = Tk()
print "Press a key (Escape key to exit):"
root.bind_all('<Key>', keypress)
# don't show the tk window
root.withdraw()
tksupport.install(root)