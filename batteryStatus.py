import os
import time
import threading

flag = ''
flg = True

def wait():
    time.sleep(70)
    flg = True

t = threading.Thread(target = wait)
while True:
    op = os.popen('pmset -g batt').read()
    #print(op)
    source = op.split('\n')[0]
    if flag != source:
        os.system(f'say {source}')
        flag = source
        per0 = op.split('\t')[1]
        per = per0[:2]
        print(per)
##        h = op.split(':')[0]
##        hours = h[-2:]
##        m = op.split(':')[1]
##        mins = m[:2]
##        print(hours)
        if 'AC Power' in source:
            os.system(f'say charging the battery from {per} percent')
        else:
            os.system(f'say current battery {per} percent')
            
    if not int(per) % 5 and flg :
        if 'AC Power' in source:
            os.system(f'say battery level has been increased to {per} percent')
            t.start()
            flg = False
        else:
            os.system(f'say battery level has been decreased to {per} percent')
            t.start()
            flg = False
