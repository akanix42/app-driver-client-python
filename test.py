import time

import threading



def printit():
    threading.Timer(1.0, printit).start()
    print "Hello, World!"

def block_forever(run_event):
    while run_event.is_set():
        try:
            import time
            print "blocking"
            time.sleep(5)
        except KeyboardInterrupt:
            return


# printit()

bonuses_count = 0
run_event = threading.Event()
run_event.set()


def count_bonuses(run_event):
    if not run_event.is_set():
        return

    global bonuses_count
    # paddle = count(paddle) # something your logic part here
    bonuses_count += 20
    if (bonuses_count == 200):
        return
    print "counting bonuses :- ", (bonuses_count)
    t = threading.Timer(1.0, count_bonuses, (run_event,)).start()

# t = threading.Timer(1.0, count_bonuses, (run_event,))
# t.start()
print('next thread')
b = threading.Thread(target = block_forever, args = (run_event,))
b.start()
# b.join()
print ('block finished')


# try:
#     while 1:
#         time.sleep(.1)
# except KeyboardInterrupt:
#     print "attempting to close threads. "
#     run_event.clear()
#     print "threads successfully closed"
# while True:
#     try:
#         print 'Ready for input:'
#         if not keypress(click.getchar()):
#             break
#     except KeyboardInterrupt:
#         connection.close()
#         break

# root = Tk()
#
# print "Press a key (Escape key to exit):"
# root.bind_all('<Key>', keypress)
# # don't show the tk window
# root.withdraw()
# root.mainloop()
# # tksupport.install(root)
