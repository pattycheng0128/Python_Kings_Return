import threading,time

def wakeUP():
    print "threading start"
    time.sleep(10)
    print "Hello"
    print "threading end"


print "start 1"
threadObj = threading.Thread(target=wakeUP())
threadObj.start()
time.sleep(1)
print "start 2"