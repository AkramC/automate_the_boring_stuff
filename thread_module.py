import threading,time

print('Start of program')

def takeNAP():
    time.sleep(5)
    print('Wake Up!')

threadObj=threading.Thread(target=takeNAP)
threadObj.start()
print('End of program.')
